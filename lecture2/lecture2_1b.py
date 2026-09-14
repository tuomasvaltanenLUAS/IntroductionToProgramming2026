age = 35
print(age)

# let's try to combine age with some text
# if we try to combine numbers and text like this
# we'll get "TypeError" if age is not converted to string first

# this is easy to fix by using f-string (see materials
age_text = str(age)
text = "Your age is: " + age_text
print(text)