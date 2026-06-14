#create a vaeiable for weight and hight 
weight=float(input("Enter Your weight in Kilograms : "))
height=float(input("Enter Your Hight in Meters : "))

#clculate BMI 
bmi=weight/(height**2)

# display the BMI

print(f"BMI is : {bmi}")

#sample output :
#Enter Your weight in Kilograms : 55
#Enter Your Hight in Meters : 160
#BMI is : 0.0021484375