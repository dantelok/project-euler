def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num / i and num // i != num:
                divisors.append(num // i)
    return divisors

def get_abundant_numbers(n=28123):
    return [i for i in range(1, n + 1) if sum(get_divisors(i)) > i]


def non_abundant_sum(limit=28123):
    abundant_numbers = get_abundant_numbers(limit)

    is_abundant_sum = [False] * (limit + 1)

    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum > limit:
                break
            is_abundant_sum[abundant_sum] = True

    return sum(i for i in range(1, limit + 1) if not is_abundant_sum[i])

result = non_abundant_sum(28123)
print("Sum of all non-abundant sums:", result)