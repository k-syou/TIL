def is_prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

T = int(input())
arr = [int(input()) for _ in range(T)]
result = []

for num in arr:
    tmp = num
    while True:
        if is_prime(tmp):
           result.append(tmp)
           break
        tmp += 1

for res in result:
    print(res)