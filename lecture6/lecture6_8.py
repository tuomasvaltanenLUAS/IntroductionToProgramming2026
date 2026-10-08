# try-block has the code that HAS THE POTENTIAL
# to crash in some specific situation, in this case
# our code assumes user always gives a number, but what
# if they give text instead?
# except-block is launched ONLY, if the error actually happens
# print error message etc.

try:
    number = input("Give a number:\n")
    number = int(number)
    print(f"Your number: {number}")
except ValueError:
    print("You wrote text, only numbers supported. Run app again!")