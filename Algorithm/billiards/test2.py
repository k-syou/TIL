import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = "A0005_1349799"

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = "127.0.0.1"

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
# HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
HOLES = [
    [0 + 3, 0 + 3],
    [127, 0],
    [254 - 3, 0 + 3],
    [0 + 3, 127 - 3],
    [127, 127],
    [254 - 3, 127 - 3],
]
r = 5.73 / 2

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

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    ballpos = [[0] * 2 for _ in range(5)]
    target = [False] * 5
    from_white = [[0] * 2 for _ in range(5)]
    from_balls = [[0] * 6 for _ in range(5)]
    path_score = [[0] * 6 for _ in range(5)]

    # 경로의 점수값으로 가장 최적의 경로를 반환함
    def selectPath():
        mx = 0
        ball_idx = -1
        hole_idx = -1
        for i in range(5):
            for j in range(6):
                if path_score[i][j] > mx:
                    mx = path_score[i][j]
                    ball_idx = i
                    hole_idx = j
        return ball_idx, hole_idx

    # 경로 점수 입력해주는 함수
    def pathScore(idx, jdx, x1, y1, x2, y2, x3, y3):
        # 두 좌표에 다른 공의 좌표가 포함되어 있으면 검사함
        minx = min(x1, x2) - 2 * r
        maxx = max(x1, x2) + 2 * r
        miny = min(y1, y2) - 2 * r
        maxy = max(y1, y2) + 2 * r
        for i in range(5):
            if i != idx:
                if ballpos[i][0] != -1.0:
                    if minx <= ballpos[i][0] <= maxx and miny <= ballpos[i][0] <= maxy:
                        if not checkPath(x1, y1, x2, y2, ballpos[i][0], ballpos[i][1]):
                            return
        # 여기까지 통과했으면 흰공 -> 목적구 사이에 장애물 없음
        path_score[idx][jdx] += 10

        minx = min(x3, x2) - 2 * r
        maxx = max(x3, x2) + 2 * r
        miny = min(y3, y2) - 2 * r
        maxy = max(y3, y2) + 2 * r

        for i in range(5):
            if i != idx:
                if ballpos[i][0] != -1.0:
                    if minx <= ballpos[i][0] <= maxx and miny <= ballpos[i][0] <= maxy:
                        if not checkPath(x2, y2, x3, y3, ballpos[i][0], ballpos[i][1]):
                            return
        path_score[idx][jdx] += 5
        # 여기까지 통과했으면 목적구 -> 구멍 사이에 장애물 없음

        a = getDegree(x1, y1, x2, y2)
        b = getDegree(x2, y2, x3, y3)
        deg_diff = a - b

        # 흰공 -> 목적구의 각도와 목적구 -> 구멍의 각도 차이가 적으면 쉬운 경로임
        if abs(deg_diff) < 30:
            score = (100 - deg_diff) / 100
            path_score[idx][jdx] += score * 2

        # 목적구 -> 구멍의 거리가 짧으면 쉬움
        bx, by = x3 - x2, y3 - y2
        hd = math.sqrt(bx**2 + by**2)
        if hd < 100:
            score = (100 - hd) / 100
            path_score[idx][jdx] += score * 1.5

        # 흰공 -> 목적구 거리가 짧으면 쉬움
        ax, ay = x2 - x1, y2 - y1
        ad = math.sqrt(ax**2 + ay**2)
        if ad < 100:
            score = (100 - ad) / 100
            path_score[idx][jdx] += score

    # 두 좌표 사이에 장애물이 있는지 확인하는 함수
    def checkPath(x1, y1, x2, y2, x3, y3):
        ax = x2 - x1
        ay = y2 - y1
        d = math.sqrt(ax**2 + ay**2)
        num = ((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((x2 * y1) + (x3 * y2) + (x1 * y3))
        dist = num / d
        if abs(dist) < 2 * r:
            return False
        return True

    # 두 좌표의 각도를 반환
    def getDegree(x1, y1, x2, y2):
        a = x2 - x1
        b = y2 - y1
        theta = math.atan2(a, b)
        return math.degrees(theta)

    def isPossible(x1, y1, x2, y2, x3, y3, max_angle=60):
        a1 = x2 - x1
        b1 = y2 - y1
        a2 = x3 - x2
        b2 = y3 - y2

        d1 = math.sqrt(a1**2 + b1**2)  # (x1, y1)와 (x2, y2)의 길이
        d2 = math.sqrt(a2**2 + b2**2)  # (x2, y2)와 (x3, y3)의 길이

        if d1 == 0 or d2 == 0:
            return False

        dot_product = a1 * a2 + b1 * b2
        cos_theta = dot_product / (d1 * d2)
        theta = math.degrees(math.acos(max(-1, min(1, cos_theta))))

        return theta <= max_angle

    # 가중치를 이용해 각도를 조정함
    def degreeModify(x, y):
        print(f"흰공 -> 목표공 각도 : {x}")
        print(f"목표공 -> 목표구멍 각도 : {y}")
        modifydeg = y - x
        if modifydeg > 0:
            a = (100 - (100 - modifydeg)) / 100
            res = x - a * 3.8
            return res
        elif modifydeg < 0:
            a = (100 - (100 - abs(modifydeg))) / 100
            res = x + a * 3.8
            return res
        else:
            return x

    # 선공 후공에 맞춰 목적구를 설정
    if order == 1:
        target = [True, False, True, False, False]
    else:
        target = [False, True, False, True, False]

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수

    # 공 위치 배열
    for i in range(1, 6):
        ballpos[i - 1][0] = balls[i][0]
        ballpos[i - 1][1] = balls[i][1]
        if ballpos[i - 1][0] == -1.0:
            target[i - 1] = False

    # 검은공으로 목표 변경
    if target[:4] == [False, False, False, False]:
        target[4] = True

    # 흰공에서 다른 공들까지의 각도
    for i in range(5):
        from_white[i] = getDegree(
            whiteBall_x, whiteBall_y, ballpos[i][0], ballpos[i][1]
        )

    # 다른 공들에서 구멍까지의 각도
    for i in range(5):
        for j in range(6):
            if target[i] == True:
                from_balls[i][j] = getDegree(
                    ballpos[i][0], ballpos[i][1], HOLES[j][0], HOLES[j][1]
                )

    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]

    print(target)

    # 가능한 경로인지 먼저 확인한 후
    # 가능한 경로이면 경로의 점수를 계산함
    for i in range(5):
        for j in range(6):
            if target[i]:
                if isPossible(
                    whiteBall_x,
                    whiteBall_y,
                    ballpos[i][0],
                    ballpos[i][1],
                    HOLES[j][0],
                    HOLES[j][1],
                ):
                    pathScore(
                        i,
                        j,
                        whiteBall_x,
                        whiteBall_y,
                        ballpos[i][0],
                        ballpos[i][1],
                        HOLES[j][0],
                        HOLES[j][1],
                    )

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = 65

    # 공과 구멍을 선택
    ball, hole = selectPath()
    print(path_score)

    print(f"{ball+1}번 공 선택, {hole + 1}번 홀 선택")

    # 흰공 -> 선택된 공 -> 선택된 구멍의 경로의 각도를 가져옴
    deg1 = getDegree(whiteBall_x, whiteBall_y, ballpos[ball][0], ballpos[ball][1])
    deg2 = getDegree(ballpos[ball][0], ballpos[ball][1], HOLES[hole][0], HOLES[hole][1])
    print(f"수정전 각도 : {deg1}")

    # 앞서 가져온 각도를 넣어 가중치 조정
    angle = degreeModify(deg1, deg2)

    # 선택된 공과 구멍이 없으면 목적구중에 아무거나 조준함
    if ball == -1:
        for i in range(5):
            if target[i]:
                angle = getDegree(
                    whiteBall_x, whiteBall_y, ballpos[i][0], ballpos[i][1]
                )
                break

    print(f"최종각도 : {angle}")

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = "%f/%f/" % (angle, power)
    sock.send(merged_data.encode("utf-8"))
    print("Data Sent: %s" % merged_data)

sock.close()
print("Connection Closed.\n--------------------")
