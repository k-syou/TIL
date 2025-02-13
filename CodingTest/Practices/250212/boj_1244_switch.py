N = int(input())  # 1 <= N <= 100
switch = [*map(int, input().split())]
S = int(input())  # 1 <= S <= 100
# O(N*S)


def solution(s, n, switch):
    # 스위치 조절 방식
    # 0 ^ 1 = 1 | 1 ^ 1 = 0
    def man(n, switch):
        # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
        # n * i - 1: n의 배수들의 인덱스 값(-1)
        i = 1
        while n * i - 1 < N:
            switch[n * i - 1] ^= 1
            i += 1

    def woman(n, switch):
        # 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
        # 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
        switch[n] ^= 1
        i = 1
        while n - i >= 0 and n + i < N:
            if switch[n - i] != switch[n + i]:
                return  # 양쪽 번호의 값이 같지 않으면 종료
            switch[n - i] ^= 1
            switch[n + i] ^= 1
            i += 1

    if s == 1:
        man(n, switch)
    else:
        woman(n - 1, switch)


for _ in range(S):
    solution(*map(int, input().split()), switch)

for i in range(N // 20 + 1):
    # 20개씩 출력
    print(*switch[i * 20 : i * 20 + 20])

#
# i=input
# N,s,S=int(i()),[*map(int,i().split())],int(i())
(N,), s, _, *d = map(lambda x: [*map(int, x.split())], open(0))
for y, n in d:
    p = n
    n -= 1
    if y ^ 2:
        while n < N:
            s[n] ^= 1
            n += p
    else:
        s[n] ^= 1
        t = n + 1
        p -= 2
        while p >= 0 and t < N and s[p] == s[t]:
            s[p] ^= 1
            s[t] ^= 1
            t += 1
            p -= 1
*map(print, s),

(n,), l, _, *d = map(lambda x: [*map(int, x.split())], open(0))
for a, b in d:
    if a ^ 2:
        for i in range(b - 1, n, b):
            l[i] ^= 1
    else:
        for i in range(min(b, n - b + 1)):
            if l[b - 1 + i] != l[b - 1 - i]:
                break
            l[b - 1 + i] = l[b - 1 - i] = l[b - 1 + i] ^ 1
*map(print, l),
