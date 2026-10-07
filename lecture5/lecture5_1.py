# our example variables, we could ask these with input too
age = 17
city = "Rovaniemi"

# we want to give specific instructions to ADULTS
# based on the city they are in

# UNDERAGE USERS should be directed to use their own school's
# HEALTH CARE services instead

# is the user an adult?
if age >= 18:
    print("Adult! Give city-specific instructions here!")

    # at this point we can be sure that the user is at least 18 years old
    # think these nested if-statements like a FOLLOW-UP question to
    # the previous (above) if-statement
    if city == "Rovaniemi":
        print("Health care address for adults: Test Alley 12")
    elif city == "Helsinki":
        print("Health care address for adults: Somewhere Road 53")

else:
    # user is not adult, provide generic text below
    print("Underage students: contact your school's health care services!")