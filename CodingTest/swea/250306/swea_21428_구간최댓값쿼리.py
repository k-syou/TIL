import sys

input = sys.stdin.readline
mod = 10**9 + 7


def solve_case():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    # 1. prev[i] 구하기: i 왼쪽에서 arr[j] >= arr[i]인 j 중 가장 가까운 인덱스 (없으면 -1)
    prev = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        prev[i] = stack[-1] if stack else -1
        stack.append(i)

    # 2. next[i] 구하기: i 오른쪽에서 arr[j] > arr[i]인 j 중 가장 가까운 인덱스 (없으면 n)
    next_ = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        next_[i] = stack[-1] if stack else n
        stack.append(i)

    # 3. 각 대표 i가 만드는 구간의 시작점, 종료점 분포를 기록
    # 그룹별로, 즉 같은 최대값 v에 대해
    groups = {}
    for i in range(n):
        v = arr[i]
        L_val = i - (
            prev[i] if prev[i] != -1 else -1
        )  # = i - (-1) = i+1 if prev[i] 없으면
        R_val = next_[i] - i
        # 구간의 시작점은 in [prev[i]+1, i]
        a = prev[i] + 1
        b = i
        # 구간의 종료점은 in [i, next_[i]-1]
        c = i
        d = next_[i] - 1
        if v not in groups:
            # S_diff와 E_diff의 길이는 n+1 (0-indexed, 인덱스 n은 경계값)
            groups[v] = ([0] * (n + 1), [0] * (n + 1))
        S_diff, E_diff = groups[v]
        # 각 구간의 시작점에 R_val씩 기여
        S_diff[a] += R_val
        if b + 1 <= n:
            S_diff[b + 1] -= R_val
        # 각 구간의 종료점에 L_val씩 기여
        E_diff[c] += L_val
        if d + 1 <= n:
            E_diff[d + 1] -= L_val

    total_pairs = 0
    # 4. 그룹별로 누적합을 구하고, 쌍의 개수를 센다.
    for v, (S_diff, E_diff) in groups.items():
        S = [0] * n  # S[i]: 구간 시작점이 i인 구간 수
        curr = 0
        for i in range(n):
            curr += S_diff[i]
            S[i] = curr
        E = [0] * n  # E[i]: 구간 종료점이 i인 구간 수
        curr = 0
        for i in range(n):
            curr += E_diff[i]
            E[i] = curr
        # 오른쪽에서 S의 누적합 C: C[i] = S[i] + S[i+1] + ... + S[n-1]
        C = [0] * (n + 1)
        curr = 0
        for i in range(n - 1, -1, -1):
            curr += S[i]
            C[i] = curr
        # r₁ < l₂ 조건: 모든 종료점 r에서, 쌍의 수 += E[r] * C[r+1]
        group_pairs = 0
        for r in range(n - 1):
            group_pairs += E[r] * C[r + 1]
        total_pairs = (total_pairs + group_pairs) % mod
    print(total_pairs % mod)


def main():
    t = int(input().strip())
    for _ in range(t):
        solve_case()


if __name__ == "__main__":
    main()

"""
1
12
1 2 3 1 2 3 1 2 3 1 2 3
"""
