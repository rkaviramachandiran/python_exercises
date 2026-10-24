# Make a program that reads three numbers, and informs if their sum is
# divisible by 5 or not

# prompt the user to enter three numbers

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the  third number: "))

result=(number1+number2+number3)/5

if (result%5==0):
    print(f"the sum of three number {result} is divisible by 5 ")
else:
    print(f"the sum of three number {result} is not divisible by 5")


# sample output1

# Enter the first number: 100
# Enter the second number: 200
# Enter the  third number: 300
# the sum of three number 120.0 divisible by 5 

# sample output2

# Enter the first number: 240
# Enter the second number: 400
# Enter the  third number: 303 
# the sum of three number 188.6 not divisible by 5