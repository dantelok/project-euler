import math

def digit_canceling_fraction():
    candidates = []
    for numerator in range(11, 99):
        for denominator in range(numerator+1, 100):
            fraction = numerator / denominator

            print(f"Before canceling: {numerator} / {denominator}")

            numerator_lst = [num for num in list(str(numerator)) if num not in list(str(denominator)) or num == '0']
            denominator_list = [num for num in list(str(denominator)) if num not in list(str(numerator)) or num == '0']

            if len(numerator_lst) != 1 or len(denominator_list) != 1:
                continue
            canceled_numerator = int(''.join(numerator_lst))
            canceled_denominator = int(''.join(denominator_list))
            if canceled_numerator == 0 or canceled_denominator == 0:
                continue
            print(f"After canceling: {canceled_numerator} / {canceled_denominator}")

            if fraction == canceled_numerator / canceled_denominator:
                candidates.append((numerator, denominator))
    return candidates


fractions = digit_canceling_fraction()
print(fractions)

product_numerator = math.prod([numerator for numerator, denominator in fractions])
product_denominators = math.prod([denominator for numerator, denominator in fractions])
print(f"product: {product_numerator} / {product_denominators}")

