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


def prime(n):
    count = 1
    prime_num = 2
    while count <= n:
        if is_prime(prime_num):
            count += 1
            if count <= n:
                prime_num += 1
        else:
            prime_num += 1

    return prime_num

print(prime(10001))




