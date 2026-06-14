#Write a program that prompts the user for two numbers and
#displays the addition, subtraction, multiplication, and division
#between them.
# Create Varuable for get input from user
num1=float(input("Enter The First number :"))
num2=float(input("Enter The Second number :"))

# preform arithmetic operation
addition=num1+num2
substractiobn=num1-num2
multipication=num1*num2
devision=num1/num2

#print the operation 

print(f"Addition is : {addition}")
print(f"Substraction is : {substractiobn}")
print(f"multiplication is : {multipication}")
print(f"devision is : {devision}")

#sample output is :
#Enter The First number :76
#Enter The Second number :56
#Addition is : 132.0
#Substraction is : 20.0
#multiplication is : 4256.0
#devision is : 1.3571428571428572