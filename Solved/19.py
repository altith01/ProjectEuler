# Counting Sundays

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    if month ==4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31


date = [1, 1, 1900]

relative_day = 1

answer = 0

while date[2] <= 2000:
    while date[1] <= 12:
        while date[0] <= days_in_month(date[1], date[2]):
            if relative_day % 7 == 0 and date[0] == 1 and date[2] > 1900:
                answer += 1
            relative_day += 1
            date[0] += 1
        date[0] = 1
        date[1] += 1
    date[1] = 1
    date[2] += 1

print(answer)
