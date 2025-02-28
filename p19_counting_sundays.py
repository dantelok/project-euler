def counting_sundays(years):
    start_year = years[0]
    end_year = years[-1]

    dates_of_first = [0] * 7

    # 1 Jan of 1901 is Tue
    dates_of_first[1] = 365 * (start_year - 1900) % 7

    # Get every month
    months_total = []
    for year in range(start_year, end_year + 1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            months_total.append([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
        else:
            months_total.append([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

    # Calculate first date of each month
    cur = 2
    for months in months_total:
        for day in months:
            cur += day % 7
            if cur > 7:
                cur -= 7
            dates_of_first[cur-1] += 1
    return dates_of_first[6]

print(counting_sundays([1901, 2000]))

