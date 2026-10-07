# application: calculate train ticket price

# the logic is this:

# students get 50% discount always
# other users pay full price + 2.5€ service fee added
# if the ticket is over 100€, no service fee

# ask the user for the needed vairables, convert price to decimal
status = input("Student or other? (s/o)\n")
price = input("Original ticket price? (€)\n")
price = float(price)

# make two different "lanes" for students and other customers
if status == "s":
    # student-specific logic
    # students get 50% discount
    price = price * 0.5

elif status == "o":
    # other users logic here

    # ONLY ADD service fee, if ticket is under 100€
    if price < 100:
        price = price + 2.5


# round the result to two decimals (because this is money)
# and print WHATEVER the price is at this point
price = round(price, 2)
print(f"Final price: {price} €")