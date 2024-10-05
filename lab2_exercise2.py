# Diong, Shan Marc C.
# BSCpE 2-2
# October 5, 2024

# Exercise 2: Compute the cube of integers in an array.
# The program should ask the user for the size of the array, then for the elements of the array, and it should display the cube of each element.

# Word Colors
red = "\033[0;31m"
yellow = "\033[1;33m"
green = "\033[0;32m"

# Ask the user for the size of the array
array_size = int(input(green + "Please enter the size of the array: "))

# Ask the user to input the elements of the array, separated by spaces
array_elements = list(map(int, input("Please enter the elements of the array separated by spaces: ").split()))

# Convert the input string of numbers into an array of integers
if len(array_elements) != array_size:
    print(red + f"\nError! You need to enter exactly {array_size} array elements!")
else:
    cube_elements = [str(element ** 3) for element in array_elements]

    # Print result separated by commas
    print(f"\nThe cube of each elements are: {yellow + ', '.join(cube_elements)}")

# End
