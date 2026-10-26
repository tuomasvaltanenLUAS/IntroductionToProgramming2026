# list of cities
cities = ["Rovaniemi", "Helsinki", "Athens", "miami", "Madrid", "Stockholm"]

print("Original order:")
print(cities)

# sort the list, approach 1, modifies original order
# cities.sort()

# sort the list, approach 2, you can save the sorted version
# into a new variable, and leave the original data in its original order
# sorted_cities = sorted(cities)

# you can use lambda to sort the values REGARDLESS of lowercase/uppercase letters
cities.sort(key=lambda v: v.upper())

print("After sorting:")
print(cities)