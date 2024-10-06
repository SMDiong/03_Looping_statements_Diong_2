# Diong, Shan Marc C.
# BSCpE 2-2
# October 5, 2024

# Exercise 2: Compute the cube of integers in an array.
# The program should ask the user for the size of the array, then for the elements of the array, and it should display the cube of each element.

# Ask the user for the size of the array
array_size = int(input("Please enter the size of the array: "))

# Ask the user to input the elements of the array, separated by spaces
array_elements = list(map(int,input("Please enter the elements of the array separated by spaces: ").split()))

# Convert the input string of numbers into an array of integers
if len(array_elements) != array_size:
    print(f"\nError! You need to enter {array_size} array elements exactly.")
else:
    cube_elements = [str(element ** 3) for element in array_elements]

# Print result
    print(f"\nThe cube of each element are: {', '.join(cube_elements)}")

# End
