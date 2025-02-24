# 2 x 2: 4! / 2! (4-2)!
# 20 x 20: 40! / 20! (40-20)!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def lattice_path(n):
    return factorial(n*2) / (factorial(n) * factorial(n*2-n))

print(lattice_path(20))

