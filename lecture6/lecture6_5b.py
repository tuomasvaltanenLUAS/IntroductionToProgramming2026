# our test data
drinks = "water, milk, coffee, tea, soda"

# ask user for their drink selection
choice = input("What would you like to drink?\n")

# check if user's text was in original text
# in other words, is the user's word in the drinks-variable
if choice in drinks:
    print("Drink found!")
else:
    print("We don't have that, sorry!")