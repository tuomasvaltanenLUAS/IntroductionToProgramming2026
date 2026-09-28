# THIS STYLE IS OFTEN USED IN WORKING LIFE
# basically we use conditional statements ONLY
# to OVERRIDE existing variables instead
# of trying to have all the code within if/else etc. structures

# you can ask these from the user too with input
# input() => float() / int()
price = 200
age = 37

# IF USER IS UNDER 18 years old
if age < 18:
    # replace the original price with
    # OLD PRICE * 0.9 (10%)
    price = price * 0.9
else:
    # for customers over 18 years old
    # price is the old price + 4.95 € postage
    price = price + 4.95

print(f"Total price: {price} €")