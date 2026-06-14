# Write a program that calculates the perimeter and area of a
# rectangle, using the formulas P = 2(w + l) and A = wl, where w
# is the width and l is the length

# create a variable for width and leanth

weight=float(input("Enetr the weight of the rectangle : "))
lenght=float(input("Enetr the leanght of the rectangle : "))

# calculate the perimeter
perimeter=2 * (weight+lenght)

# calculate the area of arectangle
area=weight*lenght

# display the results 
print(f"perimeter of rectangle is : {perimeter}")
print(f"Area of rectangle is : {area}")

# sample output is : 
# Enetr the weight of the rectangle : 14
# Enetr the leanght of the rectangle : 26
# perimeter of rectangle is : 80.0
# Area of rectangle is : 364.0
