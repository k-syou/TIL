mapping = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(int(input())):
    tc, N = input().split()
    arr = input().split()
    arr.sort(key=lambda x: mapping.index(x))
    print(tc)
    print(*arr)
