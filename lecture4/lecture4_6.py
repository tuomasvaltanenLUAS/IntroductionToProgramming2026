# ask user a discount code
discount_code = input("Give your discount code:\n")

# let's keep our current active discount code saved in a variable
current_code = "WINTER26"

# with text data we usually only use == or !=
# we can't really use > or < with text really
# for example: if "banana" > "firetruck" => doesn't make any sense
if discount_code == current_code:
    print("Discount ADDED -> -20%")
else:
    print("Normal price.")