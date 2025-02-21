import math


def count_divisors(n):
    """Return the number of divisors of n by iterating only up to sqrt(n)."""
    cnt = 0
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            cnt += 2  # i and n//i are divisors
    if root * root == n:
        cnt -= 1  # Correct if n is a perfect square
    return cnt


def first_triangular_number_with_divisor_count(threshold):
    """Return the first triangular number with more than 'threshold' divisors."""
    n = 1
    while True:
        # Generate the nth triangular number: T(n) = n*(n+1)/2
        if n % 2 == 0:
            # If n is even, use n/2 and n+1
            a = n // 2
            b = n + 1
        else:
            # If n is odd, use n and (n+1)/2
            a = n
            b = (n + 1) // 2

        # Number of divisors of T(n) is the product of divisors of a and b.
        div_count = count_divisors(a) * count_divisors(b)

        if div_count > threshold:
            triangular_number = n * (n + 1) // 2
            return triangular_number, n, div_count

        n += 1
        print(n)


result, index, divisors = first_triangular_number_with_divisor_count(500)
print("First triangular number with over 500 divisors is:", result)
print("It is the", index, "th triangular number with", divisors, "divisors.")