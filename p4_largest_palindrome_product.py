def largest_palindrome_product(n):
    palindrome_product = []
    for i in range(10**n):
        for j in range(10**n):
            product = i * j
            string = str(product)
            if string == string[::-1]:
                palindrome_product.append(product)

    return palindrome_product

print(largest_palindrome_product(3))
print(max(largest_palindrome_product(3)))

