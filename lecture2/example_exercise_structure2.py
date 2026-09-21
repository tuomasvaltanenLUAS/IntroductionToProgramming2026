# A MORE COMPLEX VERSION OF THE PREVIOUS

# THIS EXAMPLE IS A VERY COMMON STRUCTURED
# NEEDED IN THE EXERCISES

# also on example how to ask a value from user instead

# PHASE 1
# ask all needed variables from user (input)
# and convert them to numbers if needed
# YOU CAN ASK MULTIPLE VARIABLES FROM USER

# ask the salary from user => convert to decimal (float)
salary = input("How much salary did you get this month?:\n")
salary = float(salary)
print()

# ask the savings too
savings = input("How much savings do you have:\n")
savings = float(savings)
print()

# it's also fine to combine the float + input on the same line
# savings = float(input("How much savings do you have?\n"))

# PHASE 2: the actual calculation logic of the code
# this part usually starts to grow longer and more complex
# as we go further course

# increase modifier, +5%
increase = 1.05

# combine the input variables and apply the +15% increase
total = (savings + salary) * increase

# PHASE 3 - print out the result for the user
# USE F-STRING TO COMBINE TEXT AND NUMBERS EASILY
print(f"New total sum after the increase: {total} €")
