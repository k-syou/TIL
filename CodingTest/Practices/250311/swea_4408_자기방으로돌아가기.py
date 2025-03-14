T = int(input())

def set_room_number(num):
    # 방 번호 압축
    return (int(num) - 1) // 2

for tc in range(1, T + 1):
    N = int(input())
    
    # 출발 방 -> 도착 방 위치 오름차순
    people = [sorted(map(set_room_number, input().split())) for _ in range(N)]
    
    # 동선이 겹치는 횟수 기록
    check = [0] * 201
    for a, b in people:
        for i in range(a, b + 1):
            check[i] += 1
    
    # 겹치는 횟수중 최대값이 최소 시간
    print(f"#{tc} {max(check)}")

'''
3  
4  
10 20 
30 40
50 60
70 80
2 
1 3
2 200
3
10 100
20 80
30 50
'''