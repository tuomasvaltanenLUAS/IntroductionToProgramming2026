# ask user's age (integer)
age = input("How old are you?\n")
age = int(age)

# less than 30
if age < 30:
    print("Less than 30 years old.")

# more than 30
if age >= 30:
    print("30 years old or more.")

# exactly 30
if age == 30:
    print("EXACTLY 30 years old.")

# opposite of previous condition
# something else than exactly 30
if age != 30:
    print("You are NOT EXACTLY 30 years old.")

