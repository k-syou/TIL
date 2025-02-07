import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# 에라토스테네스의 체를 이용한 소수 판별
def eratosthenes(n):
    check = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if check[i]:
            for j in range(i * 2, n + 1, i):
                check[j] = False
    return check


# 이분 매칭 수행 함수 (DFS 방식)
def bpm(u, visited, pair_to, graph):
    """이분 매칭 DFS"""
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if pair_to[v] == -1 or bpm(pair_to[v], visited, pair_to, graph):
                pair_to[v] = u
                pair_to[u] = v
                return True
    return False


def max_matching(arr, graph):
    """전체 그래프에서 최대 이분 매칭을 수행"""
    pair_to = {num: -1 for num in arr}
    match_count = 0

    for num in arr:
        if pair_to[num] == -1:
            visited = {num: False for num in arr}
            if bpm(num, visited, pair_to, graph):
                match_count += 1

    return match_count * 2 == len(arr)  # 모든 숫자가 짝지어진 경우만 True 반환


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    prime_check = eratosthenes(2000)

    # 그래프 생성 (모든 가능한 소수 합 쌍)
    graph = defaultdict(list)

    for i in range(N):
        for j in range(i + 1, N):
            if prime_check[arr[i] + arr[j]]:
                graph[arr[i]].append(arr[j])
                graph[arr[j]].append(arr[i])

    first_num = arr[0]  # 첫 번째 숫자
    possible_matches = [num for num in arr[1:] if prime_check[first_num + num]]

    # print(f"첫 번째 숫자: {first_num}, 가능한 매칭 후보: {possible_matches}")  # 디버깅 출력
    # print(f"그래프 연결 상태: {dict(graph)}")  # 디버깅 출력

    result = []

    # 첫 번째 숫자와 가능한 숫자들을 하나씩 선택하여 시도
    for match in possible_matches:
        remaining = [num for num in arr if num not in (first_num, match)]

        # 새로운 그래프 생성 (first_num과 match는 고정)
        new_graph = defaultdict(list)
        for u in remaining:
            for v in graph[u]:
                if v in remaining:
                    new_graph[u].append(v)

        if max_matching(remaining, new_graph):
            result.append(match)
        #     print(f"✅ 가능: {first_num} + {match}")  # 디버깅 출력
        # else:
        #     print(f"❌ 불가능: {first_num} + {match}")  # 디버깅 출력

    # 결과 출력
    if result:
        print(*sorted(result))
    else:
        print(-1)


if __name__ == "__main__":
    main()
