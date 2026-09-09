# Make a program that reads the scores of two tests and reports whether the
# student passed (score greater than or equal to 6) or failed (score less than 6)
# in each of the tests.

score1=float(input("Enter your First score mark:"))

score2=float(input("Enter your Second  score mark:"))

if score1 >= 6:
    print("The student pass the First test")
else:
    print("The student Fail the First test")

if score2 >= 6:
    print("The student pass the Second test")

else :
    print("The student Fail the Second test")

# sample output 1
# Enter your First score mark:7
# Enter your Second  score mark:6
# The student pass the First test
# The student pass the Second test

# sample output 2
# Enter your First score mark:5
# Enter your Second  score mark:4
# The student Fail the First test
# The student Fail the Second test