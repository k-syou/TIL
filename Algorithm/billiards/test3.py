import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = "전상우1"

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
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
r = 5.73 / 2
a = r
HOLES = [
    [a, a],
    [127, a],
    [254 - a, a],
    [a, 127 - 3],
    [127, 127 - a],
    [254 - a, 127 - a],
]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]


sock = socket.socket()
print("Trying to Connect: %s:%d" % (HOST, PORT))
sock.connect((HOST, PORT))
print("Connected: %s:%d" % (HOST, PORT))

send_data = "%d/%s" % (CODE_SEND, NICKNAME)
sock.send(send_data.encode("utf-8"))
print("Ready to play!\n--------------------")


def distance(x1, y1, x2, y2):
    # 두 지점간의 거리를 구하는 함수
    width = abs(x1 - x2)
    height = abs(y1 - y2)

    return math.sqrt(width**2 + height**2)


while True:
    print("new loop")
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

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # balls_idx 로 다음 타겟을 정한다
    # 다음에 쳐야할 공을 선택하는 인덱스
    balls.append(balls[-1])
    for balls_idx in range(order, len(balls), 2):
        # 다음 공이 있는 공이라면 친다
        if (balls[balls_idx][0], balls[balls_idx][1]) != (-1, -1):
            targetBall_x = balls[balls_idx][0]
            targetBall_y = balls[balls_idx][1]
            print(targetBall_x, targetBall_y)
            break

    most_close = HOLES[0]
    min_distance = 1000

    # 현재 목적구와 가장 가까운 구멍 찾기
    # 1순위 둔각
    # 2순위 가까움
    for hole in HOLES:
        # 타깃 - 구멍멍
        d1 = distance(hole[0], hole[1], targetBall_x, targetBall_y)
        # 흰공 - 타깃깃
        d2 = distance(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)
        # 흰공 - 구멍
        d3 = distance(whiteBall_x, whiteBall_y, hole[0], hole[1])

        temp_cos = (d1**2 + d2**2 - d3**2) / (2 * d1 * d2)

        # 둔각, 가까움
        if temp_cos < -0.08 and d1 <= min_distance:
            most_close = [hole[0], hole[1]]
            min_distance = d1

    # vector: 목적구와 가장 가까운 구멍과의 좌표의 방향벡터
    vector = [
        (targetBall_x - most_close[0]) / min_distance,
        (targetBall_y - most_close[1]) / min_distance,
    ]

    # aim: 흰 공을 보내야 할 위치의 좌표
    aim = [targetBall_x + vector[0] * 2 * r, targetBall_y + vector[1] * 2 * r]

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan2(aim[0] - whiteBall_x, aim[1] - whiteBall_y)
    angle = 180 / math.pi * radian

    # radian = math.atan2(0, 0)
    # angle = 180 / math.pi * radian

    # 빗겨치기

    # power: 거리 distance에 따른 힘의 세기를 계산
    # 목표지점과 흰 색 공 간의 거리 이용
    # 목표지점/ 흰 공 거리에 따라 유연하게 선택
    power1 = distance(aim[0], aim[1], whiteBall_x, whiteBall_y) * 0.5
    power2 = distance(aim[0], aim[1], most_close[0], most_close[1]) * 0.5

    if power1 >= power2:
        power = power1

    else:
        power = power2

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
