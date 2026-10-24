# Create a program that reads three numbers and checks if their sum is
# positive, negative or equal to zero

# prompt the user to enter three numbers

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the  third number: "))

result=(number1+number2+number3)/5

if result > 0:
    print(f"yhe sum of three number {result} is positive")

elif result < 0:
    print(f"yhe sum of three number {result} is negative")

else:
    print(f"yhe sum of three number {result} is qual to zero")

# sample output 1

# Enter the first number: 64
# Enter the second number: 85
# Enter the  third number: -100
# yhe sum of three number 9.8 is positive

# sample output 2

# Enter the first number: -85
# Enter the second number: -123
# Enter the  third number: 01
# yhe sum of three number -41.4 is negative

# sample output 3

# Enter the first number: 00
# Enter the second number: 00
# Enter the  third number: 00
# yhe sum of three number 0.0 is qual to zero