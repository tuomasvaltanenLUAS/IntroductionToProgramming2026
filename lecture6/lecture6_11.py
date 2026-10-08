# THIS EXAMPLE COMBINES EVERYTHING:
# conditional statements, string operations and error management

# INSTRUCTIONS: create an application, which checks if the given
# client identifier is in correct format
# (for example, teleoperators / internet service providers etc.)

# EXAMPLE client identifier: C1234_2345

# logic: client identifier is ALWAYS 10 characters long
# sixth letter is always underscore

try:
    client = input("Give a client identifier:\n")

    text_length = len(client)

    if text_length != 10:
        print("Client identifier, incorrect length (10 required).")
    elif client[5] != "_":
        print("Underscore missing in client identifier.")
    else:
        # split the identifier into client and order number
        identifier = client[0:5]
        order = client[6:10]

        # convert the order number to int
        order = int(order)

        print(identifier)
        print(order)

except Exception as e:
    # if something goes wrong, do this lastly
    # for example: C1234_HOLA
    print(f"Error message: {e}")
    print("Incorrect client identifier.")