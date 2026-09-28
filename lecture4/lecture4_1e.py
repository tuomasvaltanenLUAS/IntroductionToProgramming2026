# # user's age, replace this with input later
age = input("How old are you?\n")
age = int(age)

# ask also the month number when they want to visit our shop
month = input("Which month you'd like to visit our store?\n")
month = int(month)

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

# since the month of the store has nothing to do
# with the user's age, have a separate if statement
if month == 7:
    print("We're closed on July.")
    print("We're back open in August, welcome!")

print("Thank you for using the application!")
