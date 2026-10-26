products = ["ORDER123_A7785_2025", "ORDER345_A33dgs54_2026",
            "ORDERghr753_A8664_2024"]

# don't use substring for splitting a string like this
# use split() instead, since with that it doesn't matter
# what length each part has, it always works!
for item in products:
    parts = item.split("_")

    # unpack the split list into variables
    order = parts[0]
    code = parts[1]
    year = parts[2]

    print(order)
    print(code)
    print(year)
    print()