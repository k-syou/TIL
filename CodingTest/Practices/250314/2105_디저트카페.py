import sys
sys.stdin = open('sample_input.txt', 'r')
def dfs(r, c, d, cafe_set:set):
    global visited, sr, sc, result
    if cafes[r][c] in cafe_set:
        return
    cafe_set.add(cafes[r][c])
    # print(r, c, d, cafe_set)
    
    nr1 = r + dr[d]
    nc1 = c + dc[d]
    
    nd = (d + 1) % 4
    nr2 = r + dr[nd]
    nc2 = c + dc[nd]
    
    visited[r][c] = 1
    if sr <= nr1 < N and 0 <= nc1 < N:
        dfs(nr1, nc1, d, cafe_set)
    if sr <= nr2 < N and 0 <= nc2 < N:
        dfs(nr2, nc2, nd, cafe_set)
    if (nr1 == sr and nc1 == sc) or (nr2 == sr and nc2 == sc):
        # print(cafe_set, len(cafe_set), sr, sc)
        result = max(result, len(cafe_set))
    cafe_set.remove(cafes[r][c])


T = int(input())
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

for tc in range(1, T + 1):
    N = int(input())
    cafes = [[*map(int, input().split())] for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = -1
    for sr in range(N-1):
        for sc in range(1, N):
            dfs(sr, sc, 0, set())
    
    print(f"#{tc} {result}")

'''
1         
4                
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5

18 18  7 16 15  3  5  6
 3  6  8  3 15 13 15  2
 4  1 11 17  3  4  3 17
16  2 18 10  2  3 11 12
11 17 16  2  9 16  5  4
17  7  6 16 16 11 15  8
 2  1  7 18 12 11  6  2
13 12 12 15  9 11 12 18
'''