import math

# Create Varuable for get input from user
num1=float(input("Enter The First number :"))
num2=float(input("Enter The Second number :"))
num3=float(input("Enter The Third number :"))


#calculate the geometric mean
product=num1*num2*num3
geometric_mean=math.pow(product,1/3)


# display the geimetric mean
print(f"Geometric mean is : {geometric_mean}")



#sample output is :
#Enter The First number :56
#Enter The Second number :65
#Enter The Third number :37
#Geometric mean is : 51.25871356899269