def sum_even_fibonacci(limit):
    first, second = 1, 2
    total = 0

    while first <= limit:
        if first % 2 == 0:
            total += first

        first, second = second, first + second

    return total


result = sum_even_fibonacci(4000000)
print(result)
