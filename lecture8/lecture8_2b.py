# create a list of products
products = ["Washing machine", "Coffee maker", "Freezer",
            "Fridge", "Toothbrush", "Microwave", "Bookshelf",
            "Oven", "Snowblower", "Mouse", "Table"]

# let's build a text variable in a loop
text = ""

# for -loop doesn't care how much stuff we have in the list
# it's going to go through all of them in order, one-by-one
for item in products:
    text = text + item + ", "

# print the text variable after loop
print(text)