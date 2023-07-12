"""Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

The functions:

are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
take one argument (the value corresponding to their names)
"""


def liters_100km_to_miles_gallon(liters):
    # Conversion factors
    one_liter = 3.785411784  # Liters to gallons conversion factor
    one_mile = 1609.344  # Meters to miles conversion factor

    # Calculate the result using the conversion formula
    result = (((100 / liters) * one_liter) / one_mile) * 1000

    # Return the result
    return result


def miles_gallon_to_liters_100km(miles):
    # Conversion factors
    one_liter = 3.785411784  # Liters to gallons conversion factor
    one_mile = 1609.344  # Meters to miles conversion factor

    # Calculate the result using the conversion formula
    result = 100 / (((miles / 1000) * one_mile) / one_liter)

    # Return the result
    return result


# Convert liters per 100 kilometers to miles per gallon
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))

# Convert miles per gallon to liters per 100 kilometers
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
