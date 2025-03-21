def cal(op, num1, num2):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


def backtrack(i, ops, nums, tot):
    global max_v, min_v
    # print(i, tot)
    if i == N:
        max_v = max(max_v, tot)
        min_v = min(min_v, tot)
        return
    
    for o in range(4):
        if ops[o] == 0:
            continue
        ops[o] -= 1
        n_tot = cal(o, tot, nums[i])
        backtrack(i + 1, ops, nums, n_tot)
        ops[o] += 1
    

T = int(input()) + 1
for tc in range(1, T):
    N = int(input())
    ops = [*map(int, input().split())]
    nums = [*map(int, input().split())]
    max_v = -float('inf')
    min_v = float('inf')
    backtrack(1, ops, nums, nums[0])
    res = max_v - min_v
    print(max_v, min_v)
    print(f"#{tc} {res}")
    
'''
1
5
2 1 0 1
3 5 3 7 9
'''