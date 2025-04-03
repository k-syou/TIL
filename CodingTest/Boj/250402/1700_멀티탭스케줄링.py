"""
<문제요약>
멀티탭에 전기용품을 넣는 순서가 주어진다
멀티탭에 전기용품이 꽂혀있는 경우 무시하고, 멀티탭에 자리가 있는 경우 그냥 넣는다
멀티탭에 자리가 없는 경우 멀티탭에서 전기용품을 빼고 새로운 전기용품을 넣는다
이때 가장 적게 플러그를 뽑는 횟수를 구하라

<제한사항>
1 <= N <= 100
1 <= K <= 100

<입력>
N, K = 멀티탭 구멍개수, 전기용품 총 사용횟수
A0, A1, ... AK-1 = 전기용품 사용 순서

<출력>
가장 적게 플러그를 뽑는 횟수

<문제풀이>
순서가 정해져 있기 때문에 결국에는 이미 꽃혀있는 전기용품 중 어떤 것을 빼는 것이 가장
효율적인지 판단해야 한다. 이때 멀티탭에 꽂혀있는 전기용품의 사용 시점을 확인하여
가장 나중에 사용되는 전기용품을 빼는 것이 가장 효율적이다.

1. 멀티탭에 전기용품이 꽂혀있는지 확인한다
2. 멀티탭에 자리가 있는지 확인한다
3. 멀티탭에 자리가 없는 경우 멀티탭에서 전기용품을 빼고 새로운 전기용품을 넣는다
4. 멀티탭에서 전기용품을 빼는 경우는 멀티탭에 꽂혀있는 전기용품 중 가장 나중에 사용되는 전기용품을 뺀다
5. 가장 적게 플러그를 뽑는 횟수를 구한다.
"""
N, K = map(int, input().split())
arr = [*map(int, input().split())]  # 전기용품 사용 순서
multitap = set()  # 멀티탭에 꽂혀있는 전기용품
use_count = 0  # 멀티탭에 사용중인 전기용품 개수
unplug_count = 0  # 플러그를 뽑는 횟수
for i in range(K):
    current = arr[i]  # 현재 사용할 전기용품
    # 1. 멀티탭에 전기용품이 꽂혀있는지 확인한다
    if current in multitap:
        continue
    
    # 2. 멀티탭에 자리가 있는지 확인한다
    if use_count < N:
        use_count += 1
        multitap.add(current)
        continue
    
    # 3. 멀티탭에 자리가 없는 경우 멀티탭에서 전기용품을 빼고 새로운 전기용품을 넣는다
    used = {}  # 멀티탭에 꽂혀있는 전기용품의 사용 시점
    for j in multitap:
        used[j] = float('inf')
        for k in range(i + 1, K):
            if j == arr[k]:
                used[j] = k
                break
    
    # 4. 멀티탭에서 전기용품을 빼는 경우는 멀티탭에 꽂혀있는 전기용품 중 가장 나중에 사용되는 전기용품을 뺀다
    unplug_number = max(used.items(), key=lambda u: u[1])[0]  # 가장 나중에 사용되는 전기용품
    multitap.remove(unplug_number)
    multitap.add(current)
    unplug_count += 1

# 5. 가장 적게 플러그를 뽑는 횟수를 구한다
print(unplug_count)
