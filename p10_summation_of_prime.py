def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check from 5 to sqrt(n), skipping even numbers
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Only check numbers of the form 6k ± 1
    return True

def summation_of_prime(n):
    total = 0
    for i in range(2, n):
        if is_prime(i):
            total += i

    return total

print(summation_of_prime(2000000))