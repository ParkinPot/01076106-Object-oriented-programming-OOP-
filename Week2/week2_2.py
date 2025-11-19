def day_of_years(day, month, year):
    if not (0 < month < 13) or day <= 0 or year <= 0:
        return "Invalid"
    month_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31, 
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if (is_leap(year)):
        month_days[2] = 29
    current_day = 0
    for i in range (1, month + 1):
        if i < month:
            current_day += month_days[i]
        else:
            if (day > month_days[i]):
                return "Invalid"
            current_day += day
    return current_day
    

def is_leap(year):
    if year <= 0:
        return "Invalid"
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def date_diff(date1, date2):
    day1, month1, year1 = map(int, date1.split("-"))
    day2, month2, year2 = map(int, date2.split("-"))
    day_order1 = day_of_years(day1, month1, year1)
    day_order2 = day_of_years(day2, month2, year2)
    if (day_order1 == "Invalid" or day_order2 == "Invalid"):
        raise ValueError()
    total_diff = 0
    if year1 == year2:
        total_diff = day_order2 - day_order1 + 1
    else:
        for current_year in range(year1, year2):
            if (current_year == year1):
                total_diff += day_in_year(current_year) - day_order1 + 1
            else:
                total_diff += day_in_year(current_year)  
        total_diff += day_order2
    return total_diff
        

def day_in_year(year):
    if (is_leap(year)):
        return 366
    return 365

try:
    date1, date2 = input().split(",")
    print(date_diff(date1, date2))
except ValueError:
    print("Invalid")