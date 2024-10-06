# Diong, Shan Marc C.
# BSCpE 2-2
# October 5, 2024

# Exercise 3: Generate a hollow square made of x based on the user's input of an integer side length n.

# Word Colors
red = "\033[0;31m"
yellow = "\033[1;33m"
green = "\033[0;32m"


# Define hollow square function
def hollow_square(n):
    # Check if the side length is less than 2
    if n < 3:
        print(red + "Side length must be at least 3 to form a hollow square!")
        return

    # Print the top of the hollow square
    print(yellow + "x" * n)

    # Loop each row
    for i in range(1, n - 1):
        print("x" + " " * (n - 2) + "x")

    # Print the bottom of the hollow square
    print("x" * n)


# Ask the user to input the side length n of the square
square_side_length = int(input(green + "Please enter the side length of the square: "))

# Print result
print('\n')
hollow_square(square_side_length)

# End