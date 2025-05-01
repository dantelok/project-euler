def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_circular_primes(limit):
    circular_primes = []
    for num in range(2, limit):
        if not is_prime(num):
            continue
        else:
            print(f"Original number: {num}")
            original_num = str(num)
            count = 0
            for _ in range(len(str(original_num))):
                num = str(num)[1:] + str(num)[0]
                print(f'After rotation: {num}')
                if not is_prime(int(num)):
                    break
                else:
                    count += 1
            if count == len(str(original_num)):
                circular_primes.append(num)

    return circular_primes

n = 1000000
circular_primes = is_circular_primes(n)
print(f'Circular primes within {n}: {circular_primes}')
print(f'Number of circular primes: {len(circular_primes)}')

