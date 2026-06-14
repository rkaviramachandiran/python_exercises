#rite a program that calculates the area of a circle from theradius, using the formula A = πr²
import math
# Create variable radius to get inupt from user

radius=float(input("Enter the Radius of circle: "))

# calulate the area of circle
area= math.pi*(radius**2)

# display the result
print(f"The Area of Circle is: {area}")

# sample output is :
# Enter the Radius of circle: 5
# The Area of Circle is: 78.53981633974483