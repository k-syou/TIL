import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = "A0005_Shinseungmin"

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
    target = []
    if order == 1:
        target.append(balls[5])
        target.append(balls[3])
        target.append(balls[1])
    else:
        target.append(balls[5])
        target.append(balls[4])
        target.append(balls[2])

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    for i in range(len(target)):
        if target[i][0] != -1:
            targetBall_x = target[i][0]
            targetBall_y = target[i][1]
    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수

    def find_hall(x, y):
        if x >= 170 and y >= 64:
            return HOLES[5]
        elif x < 85 and y >= 64:
            return HOLES[3]
        elif x >= 170 and y < 64:
            return HOLES[2]
        elif x < 85 and y < 64:
            return HOLES[0]
        elif 85 <= x < 170 and y < 64:
            return HOLES[1]
        elif 85 <= x < 170 and y > 64:
            return HOLES[4]

    Target_hall_x, Target_hall_y = find_hall(targetBall_x, targetBall_y)

    if whiteBall_y - targetBall_y == 0:
        targetBall_y = targetBall_y + 127

    elif whiteBall_x - targetBall_x == 0:
        targetBall_x = targetBall_x + 254

    def d(sx, sy, tx, ty):
        a = sx - tx
        b = sy - ty
        c = math.sqrt(a**2 + b**2)
        return c

    def find_cosi(x1, y1, x2, y2):
        D = d(x1, y1, x2, y2)
        co = (x2 - x1) / D
        si = (y2 - y1) / D
        return co, si

    def find_target_position(tx, ty, hx, hy):
        D = d(tx, ty, hx, hy)
        nD = 5.73 / D
        nx = tx - nD * (hx - tx)
        ny = ty - nD * (hy - ty)
        return nx, ny

    nx, ny = find_target_position(
        targetBall_x, targetBall_y, Target_hall_x, Target_hall_y
    )

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    x = nx - whiteBall_x
    y = ny - whiteBall_y

    x = nx - whiteBall_x
    y = ny - whiteBall_y

    radian = math.atan2(x, y)
    angle = 180 / math.pi * radian

    power = d(whiteBall_x, whiteBall_y, nx, ny) * 0.5

    if power < 30:
        power = 50

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
