def fibonacci_numbers(N: int):
    """
    N + 1 길이의 피보나치 수열을 반환
    """
    f_numbers: list = [0] * (N + 1)

    def fibonacci(n, nums):
        if n < 2:
            nums[n] = n
            return nums[n]
        f1 = nums[n - 1] if nums[n - 1] else fibonacci(n - 1, nums)
        f2 = nums[n - 2] if nums[n - 2] else fibonacci(n - 2, nums)
        nums[n] = f1 + f2
        return nums[n]

    fibonacci(N, f_numbers)
    return f_numbers


if __name__ == "__main__":
    print(fibonacci_numbers(10))
