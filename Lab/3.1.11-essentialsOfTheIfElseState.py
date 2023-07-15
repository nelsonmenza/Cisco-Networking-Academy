"""write a tax calculator.

-It should accept one floating-point value: the income.
-Next, it should print the calculated tax, rounded to full thalers. 
There's a function named round() which will do the rounding for you  you'll find it in the skeleton code in the editor.
-if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
-if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

Note: this happy country never returned any money to its citizens. 
If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.
"""

# Prompt the user to enter the annual income and convert it to a float
income = float(input("Enter the annual income: "))

if income < 85528:  # Check if the income is less than 85528
    # Calculate the tax as 18% of the income minus 556.02 (tax relief)
    tax = income * 0.18 - 556.02
elif income >= 85528:  # If the income is greater than or equal to 85528
    # Calculate the tax as 14,839.02 plus 32% of the surplus over 85528
    tax = ((income - 85528) * 0.32) + 14839.02

tax = round(tax, 0)  # Round the calculated tax to the nearest whole number

if tax <= 0:  # If the tax is less than or equal to zero
    tax = 0  # Set the tax to zero

print("The tax is:", tax, "thalers")  # Print the calculated tax
