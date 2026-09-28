number = input("Give a number:\n")
number = int(number)

# THIS IS A CLASSIC
# if remainder of the number when dividing by 2
# is EXACTLY 0 => even number
# if not (else) => odd number
if number % 2 == 0:
    print("Even number!")
else:
    print("Odd number!")