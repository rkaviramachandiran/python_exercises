# user to enter first number
number_1=int(input("Enter the first number :"))

# user to enter second number
number_2=int(input("Enter the second number :"))

# user to enter third number
number_3=int(input("Enter the third number :"))

if number_1>number_2:
    if number_1>number_3:
            print("the first number is bigger.")
    else:
            print("the third number is bigger.")
else:
    if number_2>number_3:
        print("the second number is bigger.")
    else:
        print("the third number is bigger.")        

# sample output 1
# Enter the first number :5
# Enter the second number :3
# Enter the third number :2
# the first number is bigger.

# sample output 2
# Enter the first number :60
# Enter the second number :90
# Enter the third number :80
# the second number is bigger.

# sample output 3
# Enter the first number :60
# Enter the second number :70
# Enter the third number :80
# the third number is bigger.