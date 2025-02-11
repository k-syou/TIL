for tc in range(1, int(input()) + 1):
    s = input()
    res = 0
    if s == s[::-1]:
        res = 1
    print(f"#{tc} {res}")


# for t in range(int(input())):s=input();b=s==s[::-1];print(f'#{t+1} {int(b)}')
