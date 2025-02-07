import sys
sys.setrecursionlimit(10 ** 5 * 2)
input = sys.stdin.readline

N = int(input())  # 1 <= N <= 50 (N % 2 == 0)

arr = [*map(int, input().split())]  # arr[i] <= 1000


def eratosthenes(n):
    check = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** .5)):
        for j in range(i * 2, n + 1, i):
            check[j] = False
    return check


prime_check = eratosthenes(2000)
result = []


def backtrack(couple, start):
    global result, first_couple_num, visited
    if result.count(first_couple_num):
        return False
    if couple == N:
        result.append(first_couple_num)
        return True
    visited[start] = True
    for j in range(start, N):
        if not visited[j] and prime_check[arr[start] + arr[j]]:
            visited[j] = True
            next = start + 1
            while visited[next]:
                next += 1
                if next >= N:
                    next = -1
                    break
            backtrack(couple + 2, next)
            visited[j] = False
    visited[start] = False
    return False


for i in range(1, N):
    visited = [True] + [False] * (N - 1)
    if prime_check[arr[0] + arr[i]]:
        first_couple_num = arr[i]
        visited[i] = True
        backtrack(2, 1 if i != 1 else 2)

result = result if result else [-1]
print(*sorted(result))


