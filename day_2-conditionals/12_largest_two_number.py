# user to enter first number
number_1=int(input("Enter the first number :"))

# user to enter first number
number_2=int(input("Enter the second number :"))

# check the two number by if condition 

if number_1 > number_2:
    print("the first number is bigger.")

elif number_1 < number_2:
    print("the second number is bigger.")

else:
    print("both numbers are equal.")


# sample output 1
# Enter the first number :50
# Enter the second number :45
# the first number is bigger.

# sample output 2
# Enter the first number :50
# Enter the second number :90
# the second number is bigger.

# sample output 3
# Enter the first number :50
# Enter the second number :50
# both numbers are equal.