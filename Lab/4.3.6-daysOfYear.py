"""write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, 
or returns None if any of the arguments is invalid."""


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


def day_of_year(year, month, day):
    # Check if the year is a leap year.
    year_bool = is_year_leap(year)
    add_days = 0
    if year < 1582 or month < 1 or month > 12:
        return None
    elif 1 < day > 31 or (year_bool == False and day > 28 and month == 2):
        return None
    else:
        # Calculate the number of days in each preceding month.
        for i in range(1, month):
            month_days = days_in_month(year, i)
            add_days += month_days
        return add_days + day


print(day_of_year(2000, 2, 29))
