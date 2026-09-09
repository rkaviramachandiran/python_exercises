# Make a program that reads the grades of two tests, calculates the simple
# arithmetic mean, and informs whether the student passed (average greater
# than or equal to 6) or failed (average less than 6).

score1=float(input("Enter Your grade of the first score :"))
score2=float(input("Enter Your grade of the second score :"))

average=(score1+score2)/2

if average>=6:
    print(f"The student passed with an average of {average}")

else:
    print(f"The student Failed with an average of {average}")


# sample output 1
# Enter Your grade of the first score :7
# Enter Your grade of the second score :8
# The student passed with an average of 7.5

# sample output 2
# Enter Your grade of the first score :5
# Enter Your grade of the second score :4
# The student Failed with an average of 4.5