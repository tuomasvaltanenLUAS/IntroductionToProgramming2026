# A MORE COMPLEX VERSION OF THE PREVIOUS

# THIS EXAMPLE IS A VERY COMMON STRUCTURED
# NEEDED IN THE EXERCISES

# also on example how to ask a value from user instead

# PHASE 1
# ask all needed variables from user (input)
# and convert them to numbers if needed
# YOU CAN ASK MULTIPLE VARIABLES FROM USER
savings = input("How much savings do you have:\n")
savings = float(savings)
print()

# let's also ask the user for their last month's salary
salary = input("How much salary did you get this month?:\n")
salary = float(salary)
print()

# PHASE 2: do the needed calculations as needed
# by the exercise. This part tends to be the longest phase
# in most exercises

# increase modifier, +5%
increase = 1.05

# calculate result
total = (savings + salary) * increase

# PHASE 3: print the result to the user in a nice output
print(f"New total sum after the increase: {total} €")
