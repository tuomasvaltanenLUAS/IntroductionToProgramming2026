# we typically use variables to combine them
# into some bigger calculation formula

# often these values are asked from the user instead
salary = 3100
savings = 1850
debt = 400

# calculate all money together based on variables
total_money = salary + savings - debt

# let's create a name variable too
name = "Test Person"

# print out the result with f-string
# f-string takes a little bit time to get used to
# but is by far the easiest text/variable -combination
# tool in the long run
print(f"Name: {name}, total money: {total_money} €")