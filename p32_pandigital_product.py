def is_pandigital(a, b, c):
    """Check if concatenating a, b, and c forms a 1-9 pandigital number."""
    combined = str(a) + str(b) + str(c)
    return "".join(sorted(combined)) == "123456789"

def pandigital_product():
    products = set()

    # Case 1: 1-digit × 4-digit = 4-digit (e.g., 9 × 1234 = 11106)
    for a in range(1, 10):  
        for b in range(1000, 10000):  
            c = a * b
            if is_pandigital(a, b, c):
                products.add(c)

    # Case 2: 2-digit × 3-digit = 4-digit (e.g., 39 × 186 = 7254)
    for a in range(10, 100):  
        for b in range(100, 1000):  
            c = a * b
            if is_pandigital(a, b, c):
                products.add(c)

    return sum(products)


print(pandigital_product())