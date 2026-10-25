# Write a program that prints all even numbers from 1 to
# 100.

# solution 1

num1 =1 

while num1<=100:
    if num1%2==0:
        print(num1,end=', ')
    num1+=1

# solution 2

num2=2

while num2<=100:
    print(num2 ,end=', ')
    num2+=2

# solution 3

for num3 in range (2,101,2):
    print(num3,end=', ')



# sample output

# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 
# 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 
# 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 