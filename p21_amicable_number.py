def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and n // i != n:
                divisors.append(n//i)

    return divisors

def amicable(n):
    amicable_numbers = []
    for i in range(n):
        divisors = get_divisors(i)
        d_num = sum(divisors)
        print(f'Sum of divisors of {i} is {d_num}')

        amicable_pair = sum(get_divisors(d_num))
        print(f'Sum of divisors of {d_num} is {amicable_pair}')

        if amicable_pair == i and d_num != i:
            print(f'{i} is an amicable number.')
            amicable_numbers.append(i)

    return amicable_numbers

# # Check get_divisors function
# print(get_divisors(220))

amicable_numbers = amicable(10000)

print(amicable_numbers)
print(sum(amicable_numbers))
