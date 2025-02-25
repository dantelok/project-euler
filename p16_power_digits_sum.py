def power_digits_sum(num):
    power = str(2**num)

    total = 0
    for digit in power:
        total += int(digit)

    return total


print(power_digits_sum(1000))
