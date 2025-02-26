ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"
thousand = "thousand"
and_word = "and"

def count_letters(n):
    if 1 <= n < 10:
        return len(ones[n])
    elif 10 <= n < 20:
        return len(teens[n - 10])
    elif 20 <= n < 100:
        return len(tens[n // 10]) + len(ones[n % 10])
    elif 100 <= n < 1000:
        count = len(ones[n // 100]) + len(hundred)
        if n % 100 != 0:
            count += len(and_word) + count_letters(n % 100)
        return count
    elif n == 1000:
        return len(ones[1]) + len(thousand)
    return 0


total_letters = sum(count_letters(i) for i in range(1, 1001))
print(total_letters)