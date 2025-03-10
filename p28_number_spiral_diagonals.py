def spiral_diagonals(n):
    left_diagonals, right_diagonals = 0, 0
    left_to_right_elements, right_to_left_elements = [], []

    for i in range(1, n+1):
        left_to_right_entries = 1 + i * (i-1)
        left_to_right_elements.append(left_to_right_entries)
        right_diagonals += left_to_right_entries

    # print(left_to_right_elements)
    add_element = 0
    right_to_left_entries = 1
    for i in range(1, n):
        if i % 2 != 0:
            add_element += 4

        right_to_left_entries = right_to_left_entries + add_element
        right_to_left_elements.append(right_to_left_entries)
        left_diagonals += right_to_left_entries

    # print(right_to_left_elements)
    total = left_diagonals + right_diagonals
    return total

print(spiral_diagonals(5))
print(spiral_diagonals(1001))