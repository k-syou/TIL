# 23738. 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전
T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())  # n : 배열 길이 | m : m 번 실행
    arr = [*map(int, input().split())]  # 숫자 배열

    # 순환하므로 m번 실행 후 맨앞 숫자는 m을 n으로 나눈 나머지 번째와 동일
    """
    ex) n = 3, m = 10, arr = [1, 2, 3]
        m : 1 2 3 4 5 6 7 8 9 10
        i : 1 2 0 1 2 0 1 2 0 1
        a : 2 3 1 2 3 1 2 3 1 2
    즉 10번 수행후 맨앞 arr의 값은 index = 1 번째 값(m % n)인
    a[1] = 2 임을 알 수 있음
    """
    print(f"#{tc} {arr[m % n]}")
