def is_leap(year):
    if year < 0:
        return "Invalid"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
    if not (0 < month < 13) or day <= 0 or year <= 0:
        return "Invalid"
    
    day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        day_in_month[2] = 29
    else:
        day_in_month[2] = 28
    
    if day > day_in_month[month]:
        return "Invalid"
    
    day_of_years = 0
    for i in range(1, month):
        day_of_years += day_in_month[i]
    
    day_of_years += day
    return day_of_years

try:
    day, month, year = map(int, input.split("-"))
    day_of_year_result = day_of_year(day, month, year)
    leap_year_status = is_leap(year)
    
    print("day of year:", day_of_year_result, "is_leap:", leap_year_status)
except ValueError:
    print("Invalid")
