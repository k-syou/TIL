T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 매매가의 개수
    price = [*map(int, input().split())]  # 매매가 목록
    sell_price = price[N - 1]  # 판매할 가격
    result = 0  # 이익
    for i in range(N-2, -1, -1):
        if sell_price < price[i]:
            # 판매할 가격보다 현재가가 비싼경우
            # 판매가를 갱신
            sell_price = price[i]
        else:
            # 이익값을 수정
            result += sell_price - price[i]
    # 출력Sale price
    print(f"#{tc} {result}")