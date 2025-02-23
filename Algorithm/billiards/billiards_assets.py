import math 
from collections import *

class PoolTable:
    # 당구판 객체 생성
    def __init__(self, width = 254.0, height = 127.0, R = 5.73):
        self.W = width
        self.H = height
        self.th = R / 2

    def get_holes(self):
        # 홀의 위치
        # 좌하, 우하, 좌상, 우상, 중하, 중상
        return (
            (0, 0), 
            (self.W, 0), 
            (0, self.H),
            (self.W, self.H), 
            (self.W / 2,0),
            (self.W / 2, self.H), 
            )
    
    def get_threshold(self):
        # 상 하 좌 우
        return self.H - self.th, self.th, self.th, self.W - self.th

    def get_reverse_hole(self, hole, d):
        thresholds = self.get_threshold() # 상하좌우
        thr = thresholds[d] # 임계값
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
    def __init__(self, num, x, y, R = 5.73):
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
    
    def get_reverse_ball(self, table:PoolTable, d:int):
        thresholds = table.get_threshold() # 상하좌우
        thr = thresholds[d] # 임계값
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

    
def pythagoras(a, b):
    # 피타고라스 정리 / 90도와 마주보는 빗변의 길이
    return (a ** 2 + b ** 2) ** .5

def get_theta(a, b, c):
    # 변의 길이 a, b, c가 있을 때
    # 변 a와 마주보는 각도를 출력
    cosA = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    radA = math.acos(cosA)
    A = math.degrees(radA)
    return A

def get_length_of_line(A, b, c):
    # 각도 A와 붙어있는 선분 b, c의 길이가 주어질 때
    # 각도 A와 마주보는 선분 a의 길이를 출력
    radA = math.radians(A)
    cosA = math.cos(radA)
    a = (b ** 2 + c ** 2 - 2 * b * c * cosA) ** .5
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
    area = abs((x1*y2 + x2*b + a*y1) - (x1*b + a*y2 + x2*y1))
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

def check_balls(start_ball, goal_loc, other_balls):
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

if __name__ == "__main__":
    table = PoolTable()
    b = Ball(1, 240, 115)
    rb = b.get_reverse_ball(table, 0)
    hole = (254, 127)
    # print(table.get_reverse_hole(hole, 0))
    print(table.get_reverse_hole((0, 0), 0))
    # print(rb.x, rb.y)

