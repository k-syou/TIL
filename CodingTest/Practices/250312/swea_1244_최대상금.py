import sys
sys.stdin = open("input.txt", 'r')


def get_max_v(i, cnt, nums):
    global result
    if nums == max_nums or i == len(nums):
        n_nums = nums[:]
        if cnt:
            for i in range(len(n_nums) - 1):
                if n_nums[i] == n_nums[i + 1]:
                    cnt = 0
                    break
        if len(n_nums) > 1 and cnt % 2:
            n_nums[-1], n_nums[-2] = n_nums[-2], n_nums[-1]
        result = max(result, int(''.join(n_nums)))
        return
    if cnt == 0:
        result = max(result, int(''.join(nums)))
        return
    max_idx = i
    for j in range(i + 1, len(nums)):
        if nums[j] >= nums[max_idx]:
            max_idx = j
    if max_idx == i:
        get_max_v(i + 1, cnt, nums)
    else:
        for j in range(i + 1, len(nums)):
            if nums[j] == nums[max_idx]:
                nums[i], nums[j] = nums[j], nums[i]
                get_max_v(i + 1, cnt - 1, nums)
                nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T + 1):
    nums, K = input().split()
    nums = list(nums)
    max_nums = sorted(nums, reverse=True)
    result = 0
    get_max_v(0, int(K), nums)
    print(f"#{tc} {result}")
