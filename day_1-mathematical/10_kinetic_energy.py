# Write a program that calculates the kinetic energy of a
# moving object, using the formula E = (mv²) / 2, where E is the
# kinetic energy, m is the mass of the object, and v is the velocity


mass=float(input("Enter the mass of the object : "))
velocity=float(input("Enter the velocity of the object : "))

# calculate the kinetic energy 
kinetic_energy=(mass*(velocity**2))/2

# display the result
print(f"The Kinetic Energy of a moving object is: {kinetic_energy}")

# sample output is :
# Enter the mass of the object : 10
# Enter the velocity of the object : 5
# The Kinetic Energy of a moving object is: 125.0