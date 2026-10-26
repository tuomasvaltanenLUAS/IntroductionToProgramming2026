# create a dictionary
# containing all information regarding this one person
# in one "variable"
person = {
    "name": "Test Person",
    "age": 33,
    "city": "Rovaniemi"
}

# only print the whole dictionary for testing purposes
# since otherwise you might print out sensitive information
# to the user, like passwords, session data etc.
# print(person)

# we don't usually use loops with dictionaries
# because we need to have full control what is printed what is not

# print the name of the person
print("Person's name:")
print(person['name'])

# you can also save the values into a variable
# e.g. age = person['age']

# print the age also
print("\nPerson's age:")
print(person['age'])