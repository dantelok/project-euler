def digits_n_power(n):
    equal_list = []
    upper_limit = 6 * (9 ** 5)
    for num in range(2, upper_limit):
        digit_sum = 0
        num_str = str(num)
        for digit in num_str:
            digit_sum += int(digit) ** n
        if digit_sum == num:
            # print(f'{num} = {digit_sum}')
            equal_list.append(num)

    return equal_list

# print(digits_n_power(4))
# print(sum(digits_n_power(4)))
# print(digits_n_power(5))

list_fifth_power = digits_n_power(5)
print(f'The numbers that can be written as the sum of fifth powers of their digits: {list_fifth_power}')
print(f'The sum of the numbers: {sum(list_fifth_power)}')
