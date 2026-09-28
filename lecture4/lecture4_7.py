# ask user a discount code
drink = input("What would you like you drink?\n")

# if-elif-else -> structure
# -> react to different user responses
# else => drink not found
if drink == "milk":
    print("Price of milk: 1 €")
elif drink == "coffee":
    print("Price of coffee: 10 €")
elif drink == "water":
    print("Free, drink from the tap.")
else:
    print("Drink not found.")
