def fibonacci():
    a, b = 1, 1
    idx_a, idx_b = 1, 2
    while True:
        a, b = b, a+b
        idx_a += 1
        idx_b += 1

        if len(str(b)) == 1000:
            return b, idx_b


print(fibonacci())