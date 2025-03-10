def distinct_power(lower, upper):
    elements = []
    for a in range(lower, upper+1):
        for b in range(lower, upper+1):
            c = pow(a,b)
            if c not in elements:
                elements.append(c)

    return len(elements)


print(distinct_power(2, 100))