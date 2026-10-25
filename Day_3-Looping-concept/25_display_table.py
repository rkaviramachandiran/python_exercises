# Create a program that prompts the user for a number and
# displays the table of that number using a loop.

# prompt the the user to enter the number 

num=int(input("enter your number for table (e.g 1st ,2nd ,3rd table): "))

for i in range (1,11):
    product=num*i

    print(f"{num} x {i} = {product}")

# sample output

# enter your number for table (e.g 1st ,2nd ,3rd table): 7
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70