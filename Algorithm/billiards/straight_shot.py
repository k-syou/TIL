from billiards_assets import *

def straight_shot(cue_ball:Ball, target_ball:Ball, hole, other_balls):
    cx, cy = cue_ball.get_loc() # 흰공 위치
    tx, ty = target_ball.get_loc() # 타겟공 위치

    hx, hy = hole # 홀 위치
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

    # print(f"st : cue {cue_ball.get_loc()} | tg {target_ball.get_loc()} | hole {hole}")

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

    if ct_quadrant % 2: # 1, 3 사분면
        cue_angle += (ct_quadrant - 1) * 90
        ball_angle += (ct_quadrant - 1) * 90
    else: # 2, 4 사분면
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
    return cue_angle, ball_angle, b + c, (gx, gy)