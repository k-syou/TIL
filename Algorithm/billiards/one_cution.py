from billiards_assets import *
from straight_shot import *


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
        print(
            f"one : cue {cue_ball.get_loc()} | target {r_target_ball.get_loc()} | hole : {r_hole}"
        )

        # return cue_angle, ball_angle, b + c, (gx, gy)
        st_s_result = straight_shot(cue_ball, r_target_ball, r_hole, r_other_balls)

        if st_s_result == False:
            continue

        cue_angle, ball_angle, dist, goal = st_s_result
        if not check_balls(cue_ball, goal, r_other_balls):
            continue

        if not check_balls(cue_ball, goal, t_other_balls):
            continue

        if not check_balls(r_target_ball, r_hole, r_other_balls):
            continue

        if not check_balls(target_ball, hole, t_other_balls):
            continue

        result.append((cue_angle, ball_angle, dist, goal))
    return result
