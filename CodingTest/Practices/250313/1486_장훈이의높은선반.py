# T = int(input())


# def dfs(height):
#     global min_height, x
#     x += 1
#     if B <= height:
#         if height - B < min_height:
#             min_height = height - B
#         return
    
#     for i in counting:
#         if counting[i] == 0:
#             continue
#         counting[i] -= 1
#         dfs(height + i)
#         counting[i] += 1


# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     arr = [*map(int, input().split())]
#     counting = {}
#     for h in arr:
#         tmp = counting.get(h, 0)
#         counting[h] = tmp + 1
    
#     min_height = sum(arr) - B
#     x = 0
#     dfs(0)
#     print(f"#{tc} {min_height}")
#     print(x)

T = int(input())


def dfs(idx, height):
    global min_height
    if B <= height:
        if height - B < min_height:
            min_height = height - B
        return
    
    for i in range(idx + 1, N):
        dfs(i, height + arr[i])


for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = [*map(int, input().split())]
    min_height = float('inf')
    dfs(-1, 0)
    print(f"#{tc} {min_height}")
