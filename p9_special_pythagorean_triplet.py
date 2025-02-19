def special_pythagorean_triplets():
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    print(a, b, c)
                    return a * b * c

print(special_pythagorean_triplets())