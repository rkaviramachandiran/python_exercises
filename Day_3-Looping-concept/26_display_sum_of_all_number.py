# Write a program that asks the user for a number N and
# displays the sum of all numbers from 1 to N.

# prompt the the user to enter the number 

n=int(input("Enter your number: "))

sum_of_number=0

for num in range(1,n+1):
    sum_of_number+=num
print(f"the sum of number 1 to {n} is : {sum_of_number}")

# sample output

# Enter your number: 5
# the sum of number 1 to 5 is : 15