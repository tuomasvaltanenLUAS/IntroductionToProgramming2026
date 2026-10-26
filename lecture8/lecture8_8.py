# TRY THIS IN PYTHON TUTOR
# list of cities
cities = ["rovaniemi", "oulu", "helsinki", "stockholm", "oslo", "madrid"]

# make two empty lists, to reserve for future data
# one list for LONG city names, and another for SHORT city names
long_cities = []
short_cities = []

# loop through the original cities list, AND DIVIDE/SORT THEM
# into one of thlists above based on their length
for city in cities:
    if len(city) < 7:
        short_cities.append(city)
    else:
        long_cities.append(city)


# print the result
print(short_cities)
print(long_cities)