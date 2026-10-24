#  Create a program that asks for a person's age and displays whether they
# are a child (0-12 years old), teenager (13-17 years old), adult (18-59 years old),
# or elderly (60 years old or older)

# prompt the user to enter age
age=int(input("Enter your age: "))

if age>=0 and age<=12:
    categoey="child"
elif age>=13 and age<=17:
    categoey="teenager"
    
elif age>=18 and age<=59:
    categoey="adult"
    
else:
    categoey="Elderly"

print(f"you are a {categoey}")

# sample output 

# Enter your age: 19
# you are a adult