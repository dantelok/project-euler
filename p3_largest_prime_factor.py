def largest_prime_factors(num):
    prime_factors = []
    divisor = 2
    while num != 1:
        if num % divisor == 0:
            num = num / divisor
            prime_factors.append(divisor)
        else:
            divisor += 1
    return max(prime_factors)


print(largest_prime_factors(600851475143))
