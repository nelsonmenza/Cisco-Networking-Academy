"""
Write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair 
(while only February is sensitive to the year value, your function should be universal).
"""


def is_year_leap(year):
    # Check if the year is not divisible by 100 but divisible by 400
    if year % 100 != 0 and year % 400 != 0:
        # Check if the year is divisible by 4
        if year % 4 == 0:
            return True
        else:
            return False
    # Check if the year is divisible by both 100 and 400
    elif year % 100 == 0 and year % 400 == 0:
        return True
    # Check if the year is divisible by 4 and 400
    elif year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    # This function takes two arguments: year and month.
    # It returns the number of days in the given month.

    if year < 1582 or month < 1 or month > 12:
        return None
    # Check if the year is a leap year.
    year_bool = is_year_leap(year)
    if year_bool == True and month == 2:
        return 29
    elif year_bool == False and month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31


test_years = [1582, 2000, 2016, 1987,]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
