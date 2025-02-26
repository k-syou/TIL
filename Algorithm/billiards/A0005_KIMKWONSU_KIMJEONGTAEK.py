import socket

from collections import *
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = "서울5반_김권수_김정택"

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = "127.0.0.1"

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909
BALL_RADIUS = 5.73 / 2


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
for i in range(6):
    for j in range(2):
        # if HOLES[i] in ([127, 0], [127, 127]):
        #     continue
        HOLES[i][j] = abs(HOLES[i][j] - BALL_RADIUS / (2**0.5))


class PoolTable:
    # 당구판 객체 생성
    def __init__(self, width=254.0, height=127.0, R=5.73):
        self.W = width
        self.H = height
        self.th = BALL_RADIUS / (2**0.5) - 6.5

    def get_holes(self):
        # 홀의 위치
        # 좌하, 우하, 좌상, 우상, 중하, 중상
        return (
            (0, 0),
            (self.W, 0),
            (0, self.H),
            (self.W, self.H),
            (self.W / 2, 0),
            (self.W / 2, self.H),
        )

    def get_threshold(self):
        # 상 하 좌 우
        return self.H - self.th, self.th, self.th, self.W - self.th
        # return self.H, 0, 0, self.W

    def get_reverse_hole(self, hole, d):
        thresholds = self.get_threshold()  # 상하좌우
        thr = thresholds[d]  # 임계값
        dx, dy = hole
        x_diff = abs(dx - thr)
        y_diff = abs(dy - thr)
        # print("dy",dy, thr)
        if d == 0:
            # 상 방향으로 뒤집힘
            if thr < dy:
                dy -= y_diff * 2
            else:
                dy += y_diff * 2
        elif d == 1:
            # 하 방향으로 뒤집힘
            if thr < dy:
                dy -= y_diff * 2
            else:
                dy += y_diff * 2
        elif d == 2:
            # 좌 방향으로 뒤집힘
            if thr < dx:
                dx -= x_diff * 2
            else:
                dx += x_diff * 2
        elif d == 3:
            # 우 방향으로 뒤집힘
            if thr < dx:
                dx -= x_diff * 2
            else:
                dx += x_diff * 2
        # 위치가 d 방향으로 뒤집힌 좌표를 가진 hole 리턴
        return dx, dy


class Ball:
    # 공 객체 생성
    def __init__(self, num, x, y, R=5.73):
        self.num = num  # 공의 번호
        # 공의 좌표
        self.x = x
        self.y = y
        # 공의 지름, 반지름
        self.R = R
        self.r = R / 2

    def get_loc(self):
        # 공 위치 리턴
        return self.x, self.y

    def get_reverse_ball(self, table: PoolTable, d: int):
        thresholds = table.get_threshold()  # 상하좌우
        thr = thresholds[d]  # 임계값
        dx, dy = self.get_loc()
        x_diff = abs(dx - thr)
        y_diff = abs(dy - thr)
        if d == 0:
            # 상 방향으로 뒤집힘
            dy += y_diff * 2
        elif d == 1:
            # 하 방향으로 뒤집힘
            dy -= y_diff * 2
        elif d == 2:
            # 좌 방향으로 뒤집힘
            dx -= x_diff * 2
        elif d == 3:
            # 우 방향으로 뒤집힘
            dx += x_diff * 2
        # 위치가 d 방향으로 뒤집힌 좌표를 가진 Ball 객체 생성
        return Ball(self.num, dx, dy)


def get_power(diff, dist):
    max_diff = 100
    max_dist = pythagoras(127, 254) - 50
    power = (diff / max_diff) * 40 + (dist / max_dist) * 50
    return power


def pythagoras(a, b):
    # 피타고라스 정리 / 90도와 마주보는 빗변의 길이
    return (a**2 + b**2) ** 0.5


def get_theta(a, b, c):
    # 변의 길이 a, b, c가 있을 때
    # 변 a와 마주보는 각도를 출력
    cosA = (b**2 + c**2 - a**2) / (2 * b * c)
    radA = math.acos(cosA)
    # A = math.degrees(radA)
    A = 180 / math.pi * radA
    return A


def get_length_of_line(A, b, c):
    # 각도 A와 붙어있는 선분 b, c의 길이가 주어질 때
    # 각도 A와 마주보는 선분 a의 길이를 출력
    radA = math.radians(A)
    cosA = math.cos(radA)
    a = (b**2 + c**2 - 2 * b * c * cosA) ** 0.5
    return a


def get_atan_angle(dx, dy):
    # 공과 공 or 공과 홀 사이의 각도
    return math.degrees(math.atan2(dy, dx))


def get_quadrant(sx, sy, tx, ty):
    # 4분면 검사
    if sx <= tx and sy <= ty:
        # s의 위치보다 큰 경우
        return 1
    elif sx < tx and sy > ty:
        # s의 위치보다 y좌표가 작은 경우
        return 2
    elif sx >= tx and sy >= ty:
        # s의 위치보다 작은 위치의 경우
        return 3
    elif sx > tx and sy < ty:
        # s의 위치보다 y좌표는 크고, x좌표는 작은 경우
        return 4


def cal_dist(x1, y1, x2, y2, a, b, R):
    # 선분((x1, y1) -> (x2, y2)) 과 점(a, b) 사이의 거리
    # 신발끈 공식
    area = abs((x1 * y2 + x2 * b + a * y1) - (x1 * b + a * y2 + x2 * y1))
    AB = pythagoras((x1 - x2), (y1 - y2))
    AC = pythagoras((x1 - a), (y1 - b))
    BC = pythagoras((x2 - a), (y2 - b))
    dist = area / AB
    min_x = min(x1, x2) - R
    max_x = max(x1, x2) + R
    min_y = min(y1, y2) - R
    max_y = max(y1, y2) + R

    if min_x <= a <= max_x and min_y <= b <= max_y:
        # 검사 범위안에 있는 경우, 선과 점사이의 거리 출력
        return dist
    else:
        # 아닌경우
        return min(AC, BC)


def check_balls(start_ball: Ball, goal_loc, other_balls):
    # start_ball 에서부터 goal_loc로 갈때,
    # 다른공(other_balls)이 있는 경우 확인
    R = start_ball.R
    sx, sy = start_ball.get_loc()
    gx, gy = goal_loc
    for other_ball in other_balls:
        dist = cal_dist(sx, sy, gx, gy, other_ball.x, other_ball.y, start_ball.r)
        if dist < R:
            return False
    return True


def straight_shot2(cue_ball: Ball, target_ball: Ball, hole, other_balls):
    tx, ty = target_ball.get_loc()
    hx, hy = hole
    wx, wy = cue_ball.get_loc()
    r = cue_ball.r
    # 타깃 - > 구멍
    d1 = pythagoras(hx - tx, hy - ty)
    # 흰공 - 타깃
    d2 = pythagoras(wx - tx, wy - ty)
    # 흰공 - 구멍
    d3 = pythagoras(wx - hx, wy - hy)

    temp_cos = (d1**2 + d2**2 - d3**2) / (2 * d1 * d2)

    # 둔각, 가까움
    if temp_cos > -0.08:
        return False
    # *vector, dist = dist_from_target(tx, ty, hx, hy)
    vector = [
        (tx - hx) / d1,
        (ty - hy) / d1,
    ]
    aim = [tx + vector[0] * 1.99 * r, ty + vector[1] * 1.99 * r]
    radian = math.atan2(aim[0] - wx, aim[1] - wy)
    angle = 180 / math.pi * radian

    if not check_balls(cue_ball, vector, other_balls):
        return False

    if not check_balls(target_ball, hole, other_balls):
        return False

    return angle, d1, aim


def straight_shot(cue_ball: Ball, target_ball: Ball, hole, other_balls):
    cx, cy = cue_ball.get_loc()  # 흰공 위치
    tx, ty = target_ball.get_loc()  # 타겟공 위치

    hx, hy = hole  # 홀 위치
    # 현재 공을 기준으로 타겟과 홀이
    # 같은 사분면에 있는지 확인후
    # 모든 사분면의 좌표를 1사분면에 위치하도록 변경
    ct_quadrant = get_quadrant(cx, cy, tx, ty)
    if not ct_quadrant:
        return False
    elif ct_quadrant != get_quadrant(cx, cy, hx, hy):
        # 같은 사분면 안에 없는 경우
        return False
    elif ct_quadrant == 2:
        ty += (cy - ty) * 2
        hy += (cy - hy) * 2
    elif ct_quadrant == 3:
        tx += (cx - tx) * 2
        hx += (cx - hx) * 2
        ty += (cy - ty) * 2
        hy += (cy - hy) * 2
    elif ct_quadrant == 4:
        tx += (cx - tx) * 2
        hx += (cx - hx) * 2
    # 중간 지점에 넣을 수 없는 경우
    if hx < tx:
        return False
    if cx == tx and tx != hx:
        return False

    print(f"st : cue {cue_ball.get_loc()} | tg {target_ball.get_loc()} | hole {hole}")

    # R = 공의 지름
    R = cue_ball.R
    # abx = a 에서 b까지의 x축 거리
    # aby = a 에서 b까지의 y축 거리
    # 홀(h), 흰공(c), 타겟공(t)
    hcx = hx - cx
    hcy = hy - cy
    htx = hx - tx
    hty = hy - ty
    tcx = tx - cx
    tcy = ty - cy
    # a = 흰공에서 홀까지의 거리
    a = pythagoras(hcx, hcy)
    # b = 타겟에서 홀까지의 거리
    b = pythagoras(htx, hty)
    # c = 흰공에서 타겟까지의 거리
    c = pythagoras(tcx, tcy)
    # d = 흰공의 충돌지점에서 홀까지의 거리
    d = b + R

    # 1사분면 혹은 2사분면이며,
    # 공과 홀, 타겟이 모두 같은 선상에 있는 경우
    if hx == cx:
        cue_angle = 0
        if ct_quadrant % 2 == 0:
            cue_angle = 180
        return cue_angle, cue_angle, b + c, (tx, ty)

    # 기준 비율
    stand_ratio = hcy / hcx
    # 타겟 비율
    target_ratio = tcy / tcx

    if stand_ratio == target_ratio:
        # 직선상에 존재한다.
        cue_angle = get_atan_angle(tcx, tcy)
        if ct_quadrant % 2:
            cue_angle = ct_quadrant * 90 - cue_angle
        else:
            cue_angle += (ct_quadrant - 1) * 90
        return cue_angle, cue_angle, b + c, (tx, ty)

    # C = 흰공, 흰공의 충돌지점, 홀 세 지점을 연결 하는 삼각형의 홀 부분의 각도
    C = get_theta(c, a, b)
    # e = 흰공에서 흰공의 충돌지점 까지의 거리
    e = get_length_of_line(C, a, d)

    # D = 흰공, 흰공의 충돌지점, 홀 세 지점을 연결 하는 삼각형의 흰공 부분의 각도
    D = get_theta(d, a, e)
    # X = 흰공 부터 홀까지의 각도
    X = get_theta(hcx, hcy, a)

    def get_goal_loc(e, cue_angle, cue_ball):
        # 충돌지점 위치 구하기
        alpha = 90 - cue_angle
        rad_alpha = math.radians(alpha)
        gx = math.cos(rad_alpha) * e + cue_ball.x
        gy = math.sin(rad_alpha) * e + cue_ball.y
        return gx, gy

    # ball_angle = 타겟공 부터 홀까지의 각도
    ball_angle = get_theta(htx, hty, b)
    if stand_ratio > target_ratio:
        # 흰공과 홀까지를 선분으로 이었을 때,
        # 아래쪽에 있는 경우
        cue_angle = X + D
    else:
        # 위쪽에 있는 경우
        cue_angle = X - D

    # 흰공의 충돌지점 좌표 변경
    gx, gy = get_goal_loc(e, cue_angle, cue_ball)
    if ct_quadrant == 2:
        gy -= (gy - cy) * 2
    elif ct_quadrant == 3:
        gy -= (gy - cy) * 2
        gx -= (gx - cx) * 2
    elif ct_quadrant == 4:
        gx -= (gx - cx) * 2

    angle_diff = cue_angle - ball_angle

    power = get_power(abs(angle_diff), b + c)
    standard = 1
    k = standard * (power / 110)
    if abs(angle_diff) <= 30:
        k = (standard - 0.55) * (power / 110)
    elif abs(angle_diff) <= 40:
        # k1 = 0.15
        # k2 = 0.2
        k = (standard - 0.35) * (power / 110)
    elif abs(angle_diff) <= 50:
        # k1 = 0.5
        # k2 = 0.5
        k = (standard - 0.25) * (power / 110)
    elif abs(angle_diff) <= 60:
        # k1 = 0.77
        # k2 = 0.95
        k = (standard - 0.15) * (power / 110)
    elif abs(angle_diff) <= 70:
        # k1 = 1
        # k2 = 1.1
        k = (standard - 0.1) * (power / 110)
    print(angle_diff, k)

    if abs(angle_diff) <= 20:  # 정규화 최소값
        weight = 0
    elif abs(angle_diff) <= 85:  # 정규화 최대값
        weight = (abs(angle_diff - 20)) / 65  # (각도차이 - 20) / (정규화 할 범위)
    else:
        weight = 0

    if (
        target_ball.x < 0
        or target_ball.x > 254
        or target_ball.y < 0
        or target_ball.y > 127
    ):
        angle_diff = -angle_diff
        k = 0
    if angle_diff < 0:
        cue_angle = cue_angle + weight**0.5 * k
    elif angle_diff > 0:
        cue_angle = cue_angle - weight**0.5 * k

    if ct_quadrant % 2:  # 1, 3 사분면
        cue_angle += (ct_quadrant - 1) * 90
        ball_angle += (ct_quadrant - 1) * 90
    else:  # 2, 4 사분면
        cue_angle = ct_quadrant * 90 - cue_angle
        ball_angle = ct_quadrant * 90 - ball_angle

    # cue_angle : 흰공의 각도
    # ball_angle : 타겟공의 각도
    # b + c : 총 거리
    # (gx, gy) : 흰공의 충돌지점 좌표

    if not check_balls(cue_ball, (gx, gy), other_balls):
        print("흰공이 지나가는 길에 다른 공이 존재합니다.")
        return False
    if not check_balls(target_ball, hole, other_balls):
        print(f"{target_ball.num}번 공이 지나가는 길에 다른 공이 존재합니다.")
        return False
    print(gx, gy)

    return cue_angle, ball_angle, b + c, (gx, gy)


def one_cution(
    cue_ball: Ball,
    target_ball: Ball,
    table: PoolTable,
    hole: tuple,
    other_balls: list = [Ball(0, 0, 0)],
):
    result = []
    mid_hole = table.get_holes()[4:]
    t_other_balls = list(other_balls) + [Ball(9, x, y) for x, y in mid_hole]
    for d in range(4):
        r_target_ball = target_ball.get_reverse_ball(table, d)
        r_other_balls = [ball.get_reverse_ball(table, d) for ball in other_balls] + [
            Ball(9, x, y) for x, y in mid_hole
        ]
        r_hole = table.get_reverse_hole(hole, d)

        # return cue_angle, ball_angle, b + c, (gx, gy)
        # st_s_result = straight_shot2(cue_ball, r_target_ball, r_hole, r_other_balls)
        st_s_result = straight_shot(cue_ball, r_target_ball, r_hole, r_other_balls)

        if st_s_result == False:
            continue

        cue_angle, ball_angle, dist, goal = st_s_result
        # cue_angle, dist, vector = st_s_result
        if not check_balls(cue_ball, goal, r_other_balls):
            continue

        if not check_balls(cue_ball, goal, t_other_balls):
            continue

        if not check_balls(r_target_ball, r_hole, r_other_balls):
            continue

        if not check_balls(target_ball, hole, t_other_balls):
            continue
        # print(f"{vector}, {r_target_ball.get_loc()}, {r_hole}")
        # result.append((cue_angle, dist, vector))
        result.append((cue_angle, ball_angle, dist, goal))
    return result


order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print("Trying to Connect: %s:%d" % (HOST, PORT))
sock.connect((HOST, PORT))
print("Connected: %s:%d" % (HOST, PORT))

send_data = "%d/%s" % (CODE_SEND, NICKNAME)
sock.send(send_data.encode("utf-8"))
print("Ready to play!\n--------------------")

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print("Data Received: %s" % recv_data)

    # Read Game Data
    split_data = recv_data.split("/")
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = "%d/%s" % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print(
            "\n* You will be the %s player. *\n" % ("first" if order == 1 else "second")
        )
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print("====== Arrays ======")
    for i in range(NUMBER_OF_BALLS):
        print("Ball %d: %f, %f" % (i, balls[i][0], balls[i][1]))
    print("====================")

    angle = 0.0
    power = 0.0

    # 테스트 코드
    # data_str = "64/64/190/64/-1/-1/198/78/-1/-1/198.5/63.5/"
    # data_str = "64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/"
    # data_str = "128/105/250/122/120/8/6/6/173/45/127/64/"
    # data_str = "64/64/-1/-1/120/8/-1/-1/173/45/127/64/"
    # data_str = "64/64/-1/-1/-1/-1/-1/-1/-1/-1/250/120/"
    player = 1 if order == 1 else 0

    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]
    cue_ball = Ball(0, whiteBall_x, whiteBall_y)

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    target_balls = []
    for i, (ball_x, ball_y) in enumerate(balls[1:]):
        # 타겟 공들을 리스트에 담음
        if ball_x == -1:
            continue
        num = i + 1
        if num == 5:
            num = 8
        target_ball = Ball(num, ball_x, ball_y)
        target_balls.append(target_ball)

    table = PoolTable()
    # table_map = [
    #     [" "] * (int(table.W) // 10 + 1) for _ in range(int(table.H) // 10 + 1)
    # ]
    # print(f"cue_ball : {cue_ball.x}, {cue_ball.y}")

    # table_map[round(cue_ball.y / 10)][round(cue_ball.x / 10)] = "W"
    # for target_ball in target_balls:
    #     table_map[round(target_ball.y / 10)][
    #         round(target_ball.x / 10)
    #     ] = target_ball.num
    # print("H------------------------H------------------------H")
    # for row in table_map[1:][::-1]:
    #     print("|", end="")
    #     print(*row[1:], end="")
    #     print("|")
    # print("H------------------------H------------------------H")

    # holes = table.get_holes()
    other_balls = deque(target_balls)

    import heapq

    success = []
    max_diff = 100
    max_dist = pythagoras(table.W, table.H)
    for _ in range(len(target_balls)):
        target_ball = other_balls.popleft()
        print(f"\n\nball number : {target_ball.num}")
        for hole in HOLES:
            if target_ball.num == 8:
                other_balls_nums = [other_ball.num for other_ball in other_balls]
                que8 = True
                for num in other_balls_nums:
                    if num % 2 == player:
                        que8 = False
                        break
                if not que8:
                    continue
            elif target_ball.num % 2 != player:
                continue
            result = straight_shot(cue_ball, target_ball, hole, other_balls)
            # result = False
            # result = straight_shot2(cue_ball, target_ball, hole, other_balls)
            result2 = one_cution(cue_ball, target_ball, table, hole, other_balls)
            # result2 = []
            # if result:
            #     cue_angle, dist, vector = result
            #     heapq.heappush(success, (dist, cue_angle))
            #     print(f"{vector}, {target_ball.get_loc()}, {hole}")
            # if result2:
            #     for cue_angle, dist, vector in result2:
            #         heapq.heappush(success, (dist * 1.5, cue_angle))

            if result:
                cue_angle, ball_angle, tot_dist, goals = result
                if abs(cue_angle - ball_angle) >= 90:
                    continue

                weight = abs(cue_angle - ball_angle) / max_diff

                heapq.heappush(
                    success,
                    (
                        weight,
                        get_power(abs(cue_angle - ball_angle), tot_dist),
                        abs(cue_angle - ball_angle),
                        tot_dist,
                        cue_angle,
                        ball_angle,
                        goals,
                        hole,
                        target_ball.num,
                        False,
                    ),
                )
                print(
                    f"straight   : {target_ball.num}번 공을 {cue_angle} 각도로 치면 들어갑니다! {goals}"
                )
            for r2 in result2:
                cue_angle, ball_angle, tot_dist, goals = r2
                if abs(cue_angle - ball_angle) >= 90:
                    continue
                weight = (abs(cue_angle - ball_angle) / max_diff) * 1.5 + (
                    pythagoras(target_ball.x - hole[0], target_ball.y - hole[1])
                    / max_dist
                ) * 2
                heapq.heappush(
                    success,
                    (
                        weight,
                        get_power(abs(cue_angle - ball_angle), tot_dist),
                        abs(cue_angle - ball_angle),
                        tot_dist,
                        cue_angle,
                        ball_angle,
                        goals,
                        hole,
                        target_ball.num,
                        True,
                    ),
                )
                print(
                    f"one cution : {target_ball.num}번 공을 {cue_angle} 각도로 치면 들어갑니다! {goals}"
                )

        other_balls.append(target_ball)

    idx = 0
    post_data = ""
    if not success:
        for target_ball in target_balls:
            if target_ball.num % 2 == player or target_ball.num == 8:
                tx, ty = target_ball.get_loc()
                cx, cy = cue_ball.get_loc()
                a = pythagoras(127 - ty, tx - cx)
                b = 127 - cy
                c = pythagoras(tx - cx, ty - cy)

                angle = get_theta(a, b, c)
                quadrant = get_quadrant(cx, cy, tx, ty)
                if quadrant >= 3:
                    angle = 360 - angle

                # angle = get_atan_angle(
                #     cue_ball.x - target_ball.x, cue_ball.y - target_ball.y
                # )
                break
        post_data = f"{angle}/70"

    while success:
        _w, power, diff, dist, angle, ball_angle, goals, hole, num, is_one_cution = (
            heapq.heappop(success)
        )
        # dist, angle = heapq.heappop(success)
        # 세게 치는게 좋다고 하니..
        # power = 40 + (dist / max_dist) * 60
        # if is_one_cution:
        #     diff /= 3
        # power = get_power(diff, dist)
        if power >= 100:
            power = 100
        if idx == 0:
            post_data = f"{angle}/{power}/"
            # post_data = f"{angle}/50/"
        idx += 1
        # print(
        #     "one" if is_one_cution else "str",
        #     num,
        #     round(angle, 3),
        #     round(ball_angle, 3),
        #     round(power),
        #     hole,
        # )

    print(f"\n최종적으로 {post_data} 값을 넘겨준다.")

    merged_data = post_data
    sock.send(merged_data.encode("utf-8"))
    print("Data Sent: %s" % merged_data)

sock.close()
print("Connection Closed.\n--------------------")
