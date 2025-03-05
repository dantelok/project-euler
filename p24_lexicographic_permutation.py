import itertools

# Generate all permutations of the digits 0-9 in lexicographic order
digits = "0123456789"
permutations = list(itertools.permutations(digits))

millionth_permutations = permutations[999999]
print(millionth_permutations)
millionth_permutations = "".join(permutations[999999])
print(millionth_permutations)