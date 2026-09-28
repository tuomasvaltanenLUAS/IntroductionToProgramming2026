# # user's age, replace this with input later
age = input("How old are you?\n")
age = int(age)

# conditional statement -> is age under 20?
# if it is => run the code inside the if-statement

if age < 20:
    print("You are less than 20 years old.")
elif age < 30:
    print("You are less than 30 years old.")
elif age < 40:
    print("You are less than 40 years old")
else:
    print("You are is something else.")

print("Thank you for using the application!")