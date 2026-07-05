# -*- coding: utf-8 -*-
"""
VS Code
This is an exercise given by a python book to practise input and output. The statement is:
Write a program that calculates the area of a rectangle based on the base and height specified by the user via keyboard.
Display the output using the following methods:
a. Passing values as parameters.
b. String concatenation.
c. The % operator.
d. The str.format() function.
e. F-strings.
"""

base = float(input("Write the base of the rectangle: "))
height = float(input("Write the height of the rectangle: "))
area = base*height

# Method A
print("The area of the rectangle with a base of", base, "and a height of", height, "is:", area, ".")

# Method B
print("The area of the rectangle with a base of " + str(base) + " and a height of " + str(height) + " is: " + str(area) + ".")

# Method C
print("The area of a rectangle with a base of %d and a height of %.1f is: %.1f" % (base, height, area))

# Method D
print("The area of a rectangle with a base of {ba} and a height of {he} is: {ar}".format(ba=base, he=height, ar=area))

# Method E
print(f"The area of a rectangle with a base of {base} and a height of {height} is: {area}")