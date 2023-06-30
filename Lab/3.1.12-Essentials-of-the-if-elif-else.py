"""As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.

The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.
"""
year = int(input("Enter a year: ")
           )  # Prompt the user to enter a year and convert it to an integer

# Check if the year is less than 1582 (the start of the Gregorian calendar)
if year < 1582:
    # If true, print a warning message
    print("Not within the Gregorian calendar period")
else:
    if year % 100 != 0 and year % 400 == 0:  # Check if the year is not divisible by 100 but divisible by 400
        print("Leap year")  # If true, print "Leap year"
    elif year % 100 == 0 and year % 400 == 0:  # Check if the year is divisible by both 100 and 400
        print("Leap year")  # If true, print "Leap year"
    elif year % 4 == 0:  # Check if the year is divisible by 4
        print("Leap year")  # If true, print "Leap year"
    else:
        # If none of the above conditions are true, print "Common year"
        print("Common year")
