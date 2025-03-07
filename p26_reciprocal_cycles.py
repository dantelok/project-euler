# def get_cycle_length(d):
#     remainders = {}
#     value = 1
#     position = 0
# 
#     # While value == 0, the number is divisible at the end
#     while value != 0:
#         print(f'Remainder: {remainders}\n')
#         print(f'Value: {value}\n')
#         print(f'Position: {position}\n')
#         if value in remainders:
#             return position - remainders[value]
#         remainders[value] = position
#         # Keep dividing by d, get the repeating pattern
#         value = (value * 10) % d
#         position += 1
# 
#     return 0  # No cycle (terminating decimal)
# 
# 
# def find_longest_cycle(limit):
#     max_length = 0
#     best_d = 0
# 
#     for d in range(1, limit):
#         print(f'Reciprocal of cycle {d}')
#         cycle_length = get_cycle_length(d)
#         print(f'Cycle length: {cycle_length}')
#         if cycle_length > max_length:
#             max_length = cycle_length
#             best_d = d
# 
#     return best_d, max_length

# Fermet's Little Theorem
def get_cycle_length(d):
    # If d is divisible by 2 or 5, it terminates (no cycle)
    if d % 2 == 0 or d % 5 == 0:
        return 0

    k = 1
    # Let a = 10 (decimal fractions with base 10)
    a = 10
    # Compute a^k % d iteratively
    while pow(a, k, d) != 1:
        k += 1

    # Upper bound of k = d - 1
    # Return the smallest k where 10^k = 1 mod d
    return k

def find_longest_cycle(limit):
    max_length = 0
    best_d = 0

    # Can further optimize to check only prime numbers here
    for d in range(2, limit):
        cycle_length = get_cycle_length(d)
        if d == 983:
            print(f'983 cycle_length = {cycle_length}')
        if cycle_length > max_length:
            max_length = cycle_length
            best_d = d

    return best_d, max_length

longest_d, longest_cycle = find_longest_cycle(1000)
print(f"The value of d < 1000 with the longest recurring cycle is {longest_d} with a cycle length of {longest_cycle}.")