
weekday_counter = 0
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
for year in range(1, 101):
    for month in month_days:
        days = month
        if month == 28 and year % 4 == 0 and year != 100:
            days += 1
        weekday_counter = (weekday_counter + days) % 7

        if weekday_counter == 0:
            count += 1

print(count)