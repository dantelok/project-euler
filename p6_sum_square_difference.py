def sum_square_difference(n):
    sum_of_squares = 0
    natural_sum = 0
    for num in range(1, n+1):
        sum_of_squares += num**2

    for num in range(1, n+1):
        natural_sum += num

    square_sum = natural_sum ** 2

    return square_sum - sum_of_squares


print(sum_square_difference(100))
