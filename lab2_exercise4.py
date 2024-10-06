# Diong, Shan Marc C.
# BSCpE 2-2
# October 5, 2024

# Exercise 4: Generate an inverted right triangle of asterisks * based on the user's input of height n.

# Word Colors
red = "\033[0;31m"
yellow = "\033[1;33m"
green = "\033[0;32m"


# Define inverted triangle function
def inverted_triangle(n):
    # Check if the triangle height is less than 2
    if n < 2:
        print(red + "Triangle height must be at least 2 to form an inverted right triangle!")
        return

    # Loop each row
    for i in range(n, 0, -1):
        print(yellow + '*' * i)


# Ask the user to input the height n of the triangle
inverted_triangle_height = int(input(green + "Please enter the height of an inverted right triangle: "))

# Print result
print('\n')
inverted_triangle(inverted_triangle_height)

# End