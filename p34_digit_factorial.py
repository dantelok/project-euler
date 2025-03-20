def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

def digit_factorial(n):
    factorial_sum = 0
    for num in str(n):
        factorial_sum += factorial(int(num))

    if factorial_sum == n:
        return 1
    return 0

# sum of seven 9! is a 7-digit number
upper_bound = 7 * factorial(9)
# 1 and 2 does not count
results = sum(i for i in range(3, upper_bound) if digit_factorial(i))
print(results)