# do not create random.py -file anywhere in the project
# (just like with math-module), it will confused import
import random

# generate a random number
guess = random.randint(0, 10)
print(guess)

# let's generate two random two pieces of dice
# TIP: you can duplicate a code file by selecting line
# and pressing Ctrl + D (Windows)
# CMD + D (Macintosh)
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print()
print(f"1st dice: {dice1}")
print(f"2nd dice: {dice2}")
