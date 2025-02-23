def collatz_sequences(n):
    sequences = [n]
    while n != 1:
        if n%2 == 0:
            n = n//2
            sequences.append(n)
        else:
            n = 3*n + 1
            sequences.append(n)
    return sequences

def longest_collatz(n):
    max_len = [0, 0]
    for i in range(1, n):
        print(f"Start with {i}:\n")
        sequences = collatz_sequences(i)
        print(f"Collatz Sequence: {sequences}\n")
        length = len(sequences)
        print(f"Length of Sequence: {length}\n\n")
        if length > max_len[1]:
            max_len = [i, length]
    return max_len


print(longest_collatz(1000000))
