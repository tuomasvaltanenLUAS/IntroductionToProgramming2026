# our list of dictionaries, products
products = [
    {"name": "Coffee maker", "price": 79},
    {"name": "Dishwasher", "price": 299},
    {"name": "Freezer", "price": 199},
    {"name": "Toothbrush", "price": 7},
]

# TRY THIS ALSO IN PYTHON TUTOR

print("Our available products:")
print("-----------------------")

# we have a list of dictionaries, so we need a lop
# each product (item) is on dictionary
# containing name and price
for item in products:
    name = item['name']
    price = item['price']

    # print the name and price of the ACTIVE product
    print(f"{name} - {price} €")
