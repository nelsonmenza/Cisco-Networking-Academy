"""
Your task is to write a program which:

asks the user her/his birthday 
(in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
"""

while True:
    date = input(
        "Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
    if len(date) == 8:
        break
while isinstance(date, str):
    num_lst = [int(n) for n in date]
    if sum(num_lst) > 9:
        date = sum(num_lst)
        date = str(date)
    else:
        date = sum(num_lst)


print(f"Your Digit of Life is: {date}")
