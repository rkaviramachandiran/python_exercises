# Write a program that calculates the perimeter and area of a
# triangle, using the formulas P = a + b + c and A = (b * h) / 2,
# where a, b and c are the sides of the triangle and h is the height
# relative to the side B.

a=float(input("Enter length of the side a: "))
b=float(input("Enter length of the side b: "))
c=float(input("Enter length of the side c: "))
hight=float(input("Enter the hight rtelative to the side b: "))

# calculate the perimeter of triangle 
perimeter=a+b+c

# calculate the area of triangle 
area=(b*hight)/2

# display the result
print(f"The perimeter of triangle is: {perimeter}")
print(f"The Area of triangle: {area}")

# sample output is :
# Enter length of the side a: 3  
# Enter length of the side b: 4
# Enter length of the side c: 5
# Enter the hight rtelative to the side b: 4
# The perimeter of triangle is: 12.0
# The Area of triangle: 8.0