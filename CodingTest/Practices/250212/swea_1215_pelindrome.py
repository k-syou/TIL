for tc in range(1, 11):
    K = int(input())
    board = [input() for _ in range(8)]
    n = K // 2 if K % 2 else K // 2 - 1
    res = 0
    for y in range(8):  # y : 행 or 열의 기준 값
        """
        s,e 포인터를 활용하여 펠린드롬(회문) 찾기
        s : 시작 포인터
        e : 끝 포인터

        1) K == 홀수
        "332212233"
            1. 3322s2233
            2. 332s1e233
            3. 33s212e33
            ...

        2) K == 짝수
        "3322112233"
            1. 3322se2233
            2. 332s11e233
            3. 33s2112e33
            ...
        """
        for j in range(8):  # j = 검색 시작 위치
            s = e = j  # s: 시작 지점, e: 끝 지점
            if K % 2 == 0:  # K가 짝수인 경우
                e += 1  # 끝 지점을 한칸 앞으로 검색
                if e == 8:
                    continue

            # 행 검색
            cnt = 0
            if board[y][s] == board[y][e]:
                for i in range(8):
                    if s - i < 0 or e + i >= 8 or board[y][s - i] != board[y][e + i]:
                        break
                    cnt += 1 if i == 0 and s == e else 2
                    if cnt == K:
                        res += 1
                        break

            # 열 검색
            cnt = 0
            if board[s][y] == board[e][y]:
                for i in range(8):
                    if s - i < 0 or e + i >= 8 or board[s - i][y] != board[e + i][y]:
                        break
                    cnt += 1 if i == 0 and s == e else 2
                    if cnt == K:
                        res += 1
                        break

    print(f"#{tc} {res}")
