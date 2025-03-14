# from collections import deque
# # 상 우 하 좌
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
# pipe_type = [
#     # 해당 방향으로 갈 수 있는지를 기록
#     [0, 0, 0, 0], # 빈칸
#     [1, 1, 1, 1], # ┼
#     [1, 0, 1, 0], # │
#     [0, 1, 0, 1], # ─
#     [1, 1, 0, 0], # └
#     [0, 1, 1, 0], # ┌
#     [0, 0, 1, 1], # ┐
#     [1, 0, 0, 1], # ┘
# ]


# def bfs(tunner_map, y, x, max_time):
#     q = deque()
#     q.append((y, x, 1))
#     # 결과 값
#     res_count = 1
#     # 방문기록
#     visited = [[False] * M for _ in range(N)]
#     visited[y][x] = True

#     while q:
#         ty, tx, time = q.popleft()
#         # 현재 위치의 파이프 타입
#         c_pipe = pipe_type[tunner_map[ty][tx]]
        
#         # 제한 시간을 넘긴경우
#         if time >= max_time:
#             continue
        
#         for i in range(4):
#             # 해당 방향으로 갈 수 없는 파이프인 경우
#             if not c_pipe[i]:
#                 continue
            
#             # 다음위치
#             ny = ty + dy[i]
#             nx = tx + dx[i]
            
#             # 범위 초과
#             if ny < 0 or nx < 0 or ny >= N or nx >= M:
#                 continue
            
#             # 다음 위치 파이프 타입
#             n_pipe = pipe_type[tunner_map[ny][nx]]
#             if not n_pipe[(i + 2) % 4]:
#                 # 다음 위치 파이프에 접근이 불가능 한 경우
#                 continue
            
#             # 이미 방문한 위치인 경우
#             if visited[ny][nx]:
#                 continue
#             visited[ny][nx] = True
            
#             # 갈수 있는 통로 개수 추가
#             res_count += 1
#             q.append((ny, nx, time + 1))

#     return res_count


# T = int(input())
# for tc in range(1, T + 1):
#     N, M, Y, X, L = map(int, input().split())
#     tunner_map = [[*map(int, input().split())] for _ in range(N)]
#     print(f"#{tc} {bfs(tunner_map, Y, X, L)}")


# # 2
# # 5 6 2 1 3
# # 0 0 5 3 6 0
# # 0 0 2 0 2 0
# # 3 3 1 3 7 0
# # 0 0 0 0 0 0
# # 0 0 0 0 0 0
# # 5 6 2 2 6
# # 3 0 0 0 0 3
# # 2 0 0 0 0 6
# # 1 3 1 1 3 1
# # 2 0 2 0 0 2
# # 0 0 4 3 1 1


'''
# 문제 해석
- 지도 - 이차원 배열 형태로 입력이 들어온다.
- 맨홀 뚜겅으로부터 출발해서 터널들을 이동 ⇒ 이동할 수 있는 개수를 구해라
=> BFS로 접근
   1. 큐 만들기 2. 방문기록(visited)
    - 이동방향 : 상하좌우  
    - 이동이 불가능한 경우  
        1. [델타 배열 기본] 범위 밖으로 나가면 못감
        2. [방문 기록 기본] 이미 방문한 곳은 안 감
        3. [문제 조건]
            3-1. 현재 내 위치에서 뚫려있는 곳으로만 이동 가능
            3-2. 다음 가려는 곳의 터널이 뚫려있는 곳으로만 이동 가능
            -> 이런 케이스는 델타 배열 순서와 동일하게, 이동 가능 여부를 기록해두면 좋다.

   # 큐 만들기 할 때
    q.pop(0) :리스트에서 제일 앞에 데이터를 꺼내면 리스트의 길이만큼 시간이 발생 => 시간복잡도 O(list의 길이)
      ∴  from collections import deque 사용
'''


import sys
sys.stdin = open("sample_input.txt","r")

from collections import deque


dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 터널들의 종류에 따라, 이동 가능 여부를 기록
tunnels = {
    1: [1, 1, 1, 1], # 상하좌우
    2: [1, 1, 0, 0], # 상하
    3: [0, 0, 1, 1], # 좌우
    4: [1, 0, 0, 1], # 상우
    5: [0, 1, 0, 1], # 하우
    6: [0, 1, 1, 0], # 하좌
    7: [1, 0, 1, 0]  # 상좌
}

def bfs(R,C):
    dq = deque([(R,C)])   # 처음엔 출발점인 R,C로 초기화, 계속 후보군이 계속해서 저장될 것
    visited[R][C] = 1   # 출발점 방문기록

    while dq:
        r, c = dq.popleft()  # 디큐에서 맨 왼쪽(첫번째)값 꺼내기
        dirs = tunnels[arr[r][c]] # 해당 칸의 터널 종류 선택

        for d in range(4):  # 4방향 확인
            # 아래 방법을 알기 전에는 7개의 방향에 따라 전부 for, if문을 만들었다 -> 비추

            # 출구가 안 열려 있는 경우 continue
            if dirs[d] == 0:
                continue

            nr = r + dr[d]
            nc = c + dc[d]

            ## 갈 수 있는 경로를 if문으로 만들면
            # if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and arr[nr][nc] != 0

            ## 못 가는 경우 pass -> 조건이 많아질수록 이 방법을 추천
            # 1. 범위 밖으로 넘어가면 pass
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            # 2. 이미 방문했다면 pass
            if visited[nr][nc] != 0:
                continue
            # 3. 못가면 pass
            if arr[nr][nc] == 0:
                continue

            # 다음 좌표 터널 종류 확인
            next_dirs = tunnels[arr[nr][nc]]

            # ★★★ 매우 좋은 방법 ★★★
            # 현재 상 -> 다음 하가 안 뚫려있으면 못감 반대도 동일
            # 현재 좌 -> 다음 우가 안 뚫려있으면 못감 반대도 동일
            # => 즉, 상좌 일때 하우가 안뚫려있으면 못감 반대도 동일
            # [상, 하, 좌, 우] = 인덱스 0, 1, 2, 3

            # 현재 상좌(0,2) -> next_dir 하우(1,3)이 안 뚫렸으면 못감
            if d % 2 == 0 and next_dirs[d+1] == 0:
                continue
            # 현재 하우(1,3) -> next_dor 상좌(0,2)가 안 뚫렸으면 못감
            if d % 2 == 1 and next_dirs[d-1] == 0:
                continue
            # L 시간이 넘어가면 볼 필요 없다 -> 시간 단축
            if visited[nr][nc] + 1 > L:
                continue
            # 시간을 +1 해주면서 카운팅
            visited[nr][nc] = visited[r][c] + 1
            dq.append((nr,nc))


T = int(input())
for tc in range(1,T+1):
    # 5개의 변수가 각각 의미를 가지고 있다. -> 리스트로 안 만드는게 더 편한다
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]


    # 특정 좌표까지 몇 시간이 걸렸는지 기록하기 위한 visited 생성성
    visited = [[0] * M for _ in range(N)]

    bfs(R,C)

    # visited 에서 L 시간 이하로 방문한 모든 곳을 COUNT
    cnt = 0
    for r in range(N):
        for c in range(M):
            if 0 < visited[r][c] <= L:
                cnt += 1
    
    # for row in visited:
    #     print(*row)

    print(f"#{tc} {cnt}")