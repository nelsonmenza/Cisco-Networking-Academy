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


# Test the function with test data
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    # Check if the result matches the expected test result
    if result == test_results[i]:
        print("OK")
    else:
        print("Try again")
