# Get name order
with open("p22_names.txt") as f:
    for line in f:
        # print(line.strip()[1:-1].split('","'))
        names = line.strip()[1:-1].split('","')

letter_to_number = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
    "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
    "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
}

names = sorted(names)

total_score = 0
for i in range(len(names)):
    name_score = 0
    print(f"Name: {names[i]}")
    for letter in names[i]:
        name_score += letter_to_number[letter]
    print(f"Name score: {name_score}")
    print(f"Name order: {i + 1}")
    name_score *= (i + 1)
    print(f"Total score: {name_score}")
    total_score += name_score

print(total_score)