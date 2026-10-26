# let's create a tuple for weekdays
# NOTE: use normal parentheses in tuples
weekdays = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")

# NOTE! you can't change values in a tuple
# e.g. weekdays[2] = "Someday" , will not work
# if you need to change something, re-create the whole tuple
# or just use list instead

# ask the index from the user, remember to adjust
# the index (-1) so it matches with the collection
# index better
choice = input("Which weekday would you like to know?\n")
choice = int(choice) - 1

# get the weekday and print it
# NOTE! always square brackets when accessing a collection
text = weekdays[choice]
print(text)