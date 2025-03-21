"""
5
1 2 3 4 5
4
1 3 4 6
2 3
1 1 3 -2
2 3
"""

# 펜윅 트리
# 구간합을 비트 형태로 저장하는 방식
# 구간의 형태로 가중치가 주어질 때 사용한다.
# 예를 들어 3 ~ 7까지 5라는 가중치를 준다면
# 3 4 8 16 32 ... 번호에 5라는 가중치를 주고
# 8 16 32 ... 번호에 -5로 상쇄한다.
# 그럼 결국 8 ~ 32 숫자에는 가중치가 존재하지 않는다.

# 2 ~ 5 3 을 생각해 보자
# 2 4 8 16 32 ... +3
# 6 8 16 32 ... -3
# 추후에 6을 검색한다면,
# 6(110) -> 4(100) -> 0(000) 순서로 검색할 것이고
# 가중치는 0이 된다.

# 각 트리별 의미를 알아보기
# n = 10
# tree[1] = 0001 = 1 - 1 + 1 ~ 1 = 1 ~ 1 = sum(a1)
# tree[2] = 0010 = 2 - 2 + 1 ~ 2 = 1 ~ 2 = sum(a1 ~ a2)
# tree[3] = 0011 = 3 - 1 + 1 ~ 3 = 3 ~ 3 = sum(a3)
# tree[4] = 0100 = 1 ~ 4 = sum(a1 ~ a4)
# tree[5] = 0101 = 5 ~ 5 = sum(a5)
# tree[6] = 0110 = 5 ~ 6 = sum(a5 ~ a6)
# tree[7] = 0111 = 7 ~ 7 = sum(a7)
# tree[8] = 1000 = 8 - 8 + 1 ~ 8 = 1 ~ 8 = sum(a1 ~ a8)
# tree[9] = 1001 = 9 - 1 + 1 ~ 9 = 9 ~ 9 = sum(a9)
# tree[10]= 1010 = 10 - 2 + 1 ~ 10 = 9 ~ 10 = sum(a9 ~ a10)
# tree[n] = n - (n & -n) + 1 ~ n
# tree[12] = 1100 = 12 - 4 + 1 ~ 12 = 9 ~ 12 = sum(a9 ~ a12)

# i & -i : i를 이진수로 변환했을 때 가장 왼쪽에 가까운 1의 자리수의 값
# 즉 i = 1100100 이라고 한다면, i & -i = 100 = 4 가 된다.

# 업데이트는 이와 같이 한다.
# l ~ r
# update(l, w) | update(r + 1, w)

# 만약 3 ~ 7 까지 w 만큼 가중치를 더한다고 한다면,
# update(3, w)
# 3 = 011 => tree[3] += w
# 4 = 100 => tree[4] += w
# 8 = 1000 => tree[8] += w
# (16 = 10000 > n == 10) 갱신 종료

# 7 + 1 <= n == 10 이므로
# update(8, -w)
# 8 = 1000 => tree[8] -= w
# (16 = 10000 > n == 10) 갱신 종료

# 원하는 숫자(x)의 가중치를 구하고 싶다면
# sum(a1 ~ ax)까지의 값을 구하면 된다.
# 숫자가 7 이라면,
# query(7)
# 7 = 111 => s += tree[7] (a7 ~ a7)
# 6 = 110 => s += tree[6] (a5 ~ a6)
# 4 = 100 => s += tree[4] (a1 ~ a4)
# 0 종료
# s = sum(a1 ~ a7) 이 된다

# 만약에 tree[n] 이 음수값이 된다면(범위에서 벗어난 경우)
# 결국에 a1 ~ an 을 하는 과정에서 상쇄되기 때문에 상관없다.


import sys

input = sys.stdin.readline


class Fenw:
    # 펜윅 트리
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, k):
        while i <= self.n:
            self.tree[i] += k
            i += i & -i

    def query(self, x):
        s = 0
        while x > 0:
            s += self.tree[x]
            x -= x & -x
        return s


N = int(input())
arr = [0] + [*map(int, input().split())]
fenw = Fenw(N)
res = []
for _ in range(int(input())):
    q, *data = map(int, input().split())
    if q == 1:
        i, j, k = data
        fenw.update(i, k)
        if j + 1 <= fenw.n:
            fenw.update(j + 1, -k)
    else:
        x = data[0]
        res.append(arr[x] + fenw.query(x))
print(*res, sep="\n")


# 펜윅트리 설명

# N : 노드의 개수
N = 8
# size : 트리의 크기
size = N + 1
# 펜윅 트리 초기화
fenw_tree = [0] * size

#업데이트
def update(tree, i, w, size):
    '''
    tree : 펜윅트리
    i : 시작 번호
    w : 가중치
    size : 트리의 크기

    i ~ N 까지 w 가중치를 부여한다.
    '''
    while i < size:
        tree[i] += k
        i += i & -i

"""
update 함수 시각화

열 : 트리의 인덱스
행 : update 함수 실행 시 i 위치
+  : 가중치가 더해진 위치 

   01 02 03 04 05 06 07 08
1   +  +     +           +
2      +     +           +
3         +  +           +
4            +           +
5               +  +     +
6                  +     +
7                     +  +
8                        +
다시 말해 update(tree, 1, 3, size) 를 실행하면,
1 ~ size 범위에 3의 가중치를 주는 것과 같다.
"""

"""
펜윅트리의 각 위치별 설명
Ai = i번째의 가중치
fenw_tree[1] = 0001 = A1 ~ A1
fenw_tree[2] = 0010 = A1 ~ A2
fenw_tree[3] = 0011 = A3 ~ A3
...
fenw_tree[8] = 1000 = A1 ~ A8
fenw_tree[n] = A(n-(n & -n) + 1) ~ An

n & -n 이란?
이진수로 표기했을 때 오른쪽에 가장 가까운 1의 위치를 10진수로 표기
ex ) n = 6
# 맨 앞은 부호를 나타냄(0 = +, 1 = -)
 n = 0110
-n = 1010 (2의 보수)
위 두수를 &조건으로 확인하면
n & -n = 0010 = 2
임을 알 수 있다.
"""

# 원하는 위치의 가중치의 합 구하기
def query(tree, i):
    '''
    tree : 펜윅트리
    i : 위치

    1 ~ i 범위의 가중치의 합을 출력
    '''
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s

"""
query 함수가 구해지는 과정
query(tree, 7) 이라는 함수를 실행 한다면,

1. i = 7
7 > 0 : True
    s += tree[7]
    i = 7 - (7 & -7) = 7 - (0111 & 1001) = 7 - 1 = 6

2. i = 6
6 > 0 : True
    s += tree[6]
    i = 6 - (6 & -6) = 6 - (0110 & 1010) = 6 - 2 = 4

3. i = 4
4 > 0 : True
    s += tree[4]
    i = 4 - (4 & -4) = 4 - (0100 & 1100) = 4 - 4 = 0

4. i = 0
0 > 0 : False

5. 종료
	return s

풀어서 계산해보자면,
tree[7] = A7 ~ A7
tree[6] = A5 ~ A6
tree[4] = A1 ~ A4
이므로
s = A1 ~ A7 범위의 가중치의 합 임을 알 수 있음
"""
