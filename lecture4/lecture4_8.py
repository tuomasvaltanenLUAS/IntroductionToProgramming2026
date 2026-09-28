# ask user a discount code
choice = input("Are you a student? (y/n)\n")

# if user is student
if choice == "y":
    print("This code only runs when user is a student")
    print("For example, calculate a ticket price etc.")
elif choice == "n":
    print("Calculate price for other customers etc.")
else:
    print("Incorrect selection. Please restart the application.")
