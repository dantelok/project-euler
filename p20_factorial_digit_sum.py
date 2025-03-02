def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * factorial(n-1)

def factorial_digit_sum(n):
    factorial_num = str(factorial(n))

    digit_sum = 0

    for num in factorial_num:
        digit_sum += int(num)

    return digit_sum

print(factorial_digit_sum(100))

