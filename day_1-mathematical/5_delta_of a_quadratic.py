# Write a program that calculates the delta of a quadratic equation (Δ = b² - 4ac)
# create a variable for coefficients of the quadratic equation

a=float(input("Enter the coefficients a :"))
b=float(input("Enter the coefficients b :"))
c=float(input("Enter the coefficients c :"))

# calculate the delta(Δ = b² - 4ac)
delta=b**2 - 4*a*c

# display the result
print(f"the delta of a quadratic equation is : {delta}")

# sample output is :
# Enter the coefficients a :6
# Enter the coefficients b :8
# Enter the coefficients c :10
# the delta of a quadratic equation is : -176.0