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

def generate_primes(limit):
    """Generates a list of prime numbers up to a given limit using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def count_consecutive_primes(a, b):
    """Counts how many consecutive primes are produced by the quadratic formula."""
    n = 0
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n


def find_best_coefficients(limit):
    """Finds the coefficients a and b that produce the longest sequence of primes."""
    max_n = 0
    best_a, best_b = 0, 0

    # Generate a list of primes for b values (since b must be prime)
    prime_list = generate_primes(limit)

    for b in prime_list:
        for a in range(-limit + 1, limit, 2):  # a should mostly be odd
            sequence_length = count_consecutive_primes(a, b)
            if sequence_length > max_n:
                max_n = sequence_length
                best_a, best_b = a, b

    return best_a, best_b, best_a * best_b


# Solve for the given range (-999 ≤ a ≤ 999, -1000 ≤ b ≤ 1000)
a, b, product = find_best_coefficients(1000)

print(f"Best coefficients: a = {a}, b = {b}")
print(f"Product of coefficients: {product}")