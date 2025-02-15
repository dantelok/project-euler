def gcd(a, b):
    """Computes the Greatest Common Divisor (GCD) using Euclid’s algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Computes the Least Common Multiple (LCM) using GCD."""
    return (a * b) // gcd(a, b)


def smallest_multiple(n):
    """Finds the smallest number that is evenly divisible by all numbers from 1 to n."""
    multiple = 1
    for i in range(1, n + 1):
        multiple = lcm(multiple, i)  # Compute LCM progressively
    return multiple


# Test cases
print(smallest_multiple(1))   # Output: 1
print(smallest_multiple(2))   # Output: 2
print(smallest_multiple(5))   # Output: 60
print(smallest_multiple(10))  # Output: 2520
print(smallest_multiple(20))
