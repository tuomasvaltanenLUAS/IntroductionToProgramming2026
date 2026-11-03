# another version of list of lists

# product categories in a webstore
books = ["Lord of the Rings", "Da Vinci Code", "Robinson Crusoe"]
movies = ["Interstellar", "Forrest Gump", "Jurassic Park"]

# list of lists => ALL PRODUCT CATEGORIES in one => all products
products = [books, movies]

# TRY THIS ALSO IN PYTHON TUTOR

# since products is a LIST OF LISTS
# we need a FOR loop with another FOR loop
for category in products:
    # for each PRODUCT item in CURRENT active CATEGORY
    for item in category:
        print(item)