# let's ask this from user instead
text = input("Write some text:\n")

# from first character to 10th
# REMEMBER: empty space (whitespace) is also a character
# these examples are also very helpful in exercise 4-3
subtext1 = text[0:10]
print(subtext1)

# take a partial text from the middle
# start position is at 10 (starting from 11th), until the 15th character
subtext2 = text[10:15]
print(subtext2)

# take all the characters after the 6th character
subtext3 = text[5:]
print(subtext3)

# take all the characters after the 6th character
subtext4 = text[-5:]
print(subtext4)

# EXTRA: sometimes handy, remove only the last character
# often some kind of extra mess we have to clean up
subtext5 = text[0:-1]
print(subtext5)

