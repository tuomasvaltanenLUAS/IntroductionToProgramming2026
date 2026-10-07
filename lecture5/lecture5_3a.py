# initialize our helper control boolean variable: raining
# the ONLY PURPOSE of this variable is to
# KEEP TRACK of one question: IS IT RAINING AT THE MOMENT?
raining = False

# other variables used in the code
# humidity => 0-100%
humidity = 88
temperature = -7

# in this part you would have all the possible logic
# that can alter the condition of the raining-variable
# THIS COULD BE 300-500 LINES OF CODE
if humidity > 80:
    raining = True

# another check, if temperature is subzero, it's no longer rain
# (it's something more icy at that point)
if temperature < 0:
    raining = False

# YOU COULD HAVE HUNDREDS OR THOUSANDS OF LINES OF CODE HERE
# and even more if-statement that modify the boolean

# with Boolean logic, you usually have an if-statement
# like this AT THE END OF THE CODE, which handles
# the final situation of the boolean variable

# if raining ==> if raining == True
# if not raining ==> if raining == False
if raining:
    print("It rains!")
else:
    print("It doesn't rain.")