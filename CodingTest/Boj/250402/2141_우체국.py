"""
<문제요약>
일직선 상에 N개의 마을이 있고, i번째 마을의 위치는 X[i], 마을의 인구수는 A[i]이다.
각 마을에서 사람들의 거리의 합이 최소가 되는 위치에 우체국을 세울때, 위치를 출력하시오.
단, 그러한 위치가 여러개라면, 가장 낮은 번호의 마을을 출력

<입력>
N = 마을 개수
Xi, Ai = 마을위치, 인구수

<알고리즘>
가중 중앙값, 그리디

<문제풀이>
마을을 위치 순으로 정렬할 때, 앞에서부터 인구수를 누적하여
인구수가 전체인구수의 절반을 넘을때가 중앙의 위치이다.

1. 총 인원수 구하기
2. 마을 위치 순으로 정렬하기
3. 앞쪽 마을부터 순회하며 인구수를 누적
4. 전체 인구수의 절반을 누적 인구수가 넘는 경우 해당 위치를 저장
5. 출력
"""
import sys

input = sys.stdin.readline

N = int(input())
villages = []
# 1. 총 인원수 구하기
tot = 0  # 총 인원수
for _ in range(N):
    x, a = map(int, input().split())
    villages.append((x, a))
    tot += a

# 2. 마을 위치 순으로 정렬하기
# mid = tot // 2  # Fail

# 합이 홀수인 경우 그냥 반으로 나누면 절반 이상이 아닐 수 있음
# 그래서 tot // 2 가 아닌 (tot + 1) // 2 로 변경
mid = (tot + 1) // 2  # Success
villages.sort(key=lambda v: v[0])

# 3. 앞쪽 마을부터 순회하며 인구수를 누적
peoples = 0  # 누적 인구수
res = -1  # 결과값
for i in range(N):
    peoples += villages[i][1]  # 인구수 누적
    if peoples >= mid:
        # 4. 전체 인구수의 절반을 누적 인구수가 넘는 경우 해당 위치를 저장
        res = villages[i][0]
        break
# 5. 출력
print(res)