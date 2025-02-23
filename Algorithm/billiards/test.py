from billiards_assets import *
from straight_shot import *
from one_cution import *

# 테스트 코드
# data_str = "64/64/190/64/-1/-1/198/78/-1/-1/198.5/63.5/"
# data_str = "64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/"
data_str = "128/105/250/122/120/8/6/6/173/45/127/64/"
# data_str = "64/64/-1/-1/120/8/-1/-1/173/45/127/64/"
# data_str = "64/64/-1/-1/-1/-1/-1/-1/-1/-1/250/120/"
player = 'first' # or "second" | 선후 플레이어 설정
if player == 'first':
    target = [1, 3]
else:
    target = [2, 4]
data = list(map(float, data_str[:-1].split('/')))


cue_ball = Ball(0, data[0], data[1])
target_balls = []
for i in range(2, len(data), 2):
    if data[i] < 0 or data[i + 1] < 0:
        continue
    target_balls.append(Ball(i // 2 if i // 2 < 5 else 8, data[i], data[i+1]))


table = PoolTable()
table_map = [[" "] * (int(table.W) // 10 + 1) for _ in range(int(table.H) // 10 + 1)]
print(f"cue_ball : {cue_ball.x}, {cue_ball.y}")


table_map[round(cue_ball.y / 10)][round(cue_ball.x / 10)] = "W"
for target_ball in target_balls:
    table_map[round(target_ball.y / 10)][round(target_ball.x / 10)] = target_ball.num
print("H------------------------H------------------------H")
for row in table_map[1:][::-1]:
    print("|", end="")
    print(*row[1:], end="")
    print("|")
print("H------------------------H------------------------H")

holes = table.get_holes()
other_balls = deque(target_balls)

import heapq
success = []

for _ in range(len(target_balls)):
    target_ball = other_balls.popleft()
    print(f"\n\nball number : {target_ball.num}")
    for hole in holes:
        if target_ball.num == 8:
            other_balls_nums = [other_ball.num for other_ball in other_balls]
            que8 = True
            for num in other_balls_nums:
                if num in target:
                    que8 = False
                    break
            if not que8:
                continue
        elif target_ball.num not in target:
            continue
        result = straight_shot(cue_ball, target_ball, hole, other_balls)
        result2 = one_cution(cue_ball, target_ball, table, hole, other_balls)
        if result:
            cue_angle, ball_angle, tot_dist, goals = result
            heapq.heappush(success, (abs(cue_angle - ball_angle), tot_dist, cue_angle, ball_angle, goals, hole, target_ball.num, False))
            print(f"straight   : {target_ball.num}번 공을 {cue_angle} 각도로 치면 들어갑니다! {goals}")
        for r2 in result2:
            cue_angle, ball_angle, tot_dist, goals = r2
            heapq.heappush(success, (abs(cue_angle - ball_angle) * 5, tot_dist, cue_angle, ball_angle, goals, hole, target_ball.num, True))
            print(f"one cution : {target_ball.num}번 공을 {cue_angle} 각도로 치면 들어갑니다! {goals}")
        
    other_balls.append(target_ball)

idx = 0
post_data = ""
while success:
    diff, dist, angle, ball_angle, goals, hole, num, is_one_cution = heapq.heappop(success)
    max_diff = 90
    max_dist = pythagoras(table.W, table.H)
    if is_one_cution:
        diff /= 5
    # 세게 치는게 좋다고 하니..
    power = 70 + (diff / max_diff) * 10 + (dist / max_dist) * 20
    if power >= 100:
        power = 100
    if idx == 0:
        post_data = f"{round(angle, 3)}/{round(power)}/"
    idx += 1
    print('one' if is_one_cution else "str", num, round(angle, 3), round(ball_angle, 3), round(power), hole)


print(f"\n최종적으로 {post_data} 값을 넘겨준다.")