#  Make a program that asks for two numbers and displays if the first is
# divisible by the second



# prompt the user to enter number

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))


if num1%num2 == 0:
    result="Divisible"

else:
    result="Not Divisible"

print(f"the fist number is {result} by the second number")

# sample output 

# Enter your first number: 50
# Enter your second number: 10
# the fist number is Divisible by the second number