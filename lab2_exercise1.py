# Diong, Shan Marc C.
# BSCpE 2-2
# October 5, 2024

# Exercise 1: Calculate the result of a number raised to a power using recursion.
# For example, to calculate 2^7, you multiply 2 by itself seven times.

# Define power function that use recursion
def power(base, exponent):
    # Check if exponent is Zero
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


# Ask the user for the input of values
base = int(input("Please enter the base number: "))
exponent = int(input("Please enter the exponent: "))

# Return and print result
power_result = power(base, exponent)
print(f"\n{base} raised to the power of {exponent} is: {power_result}")

# End