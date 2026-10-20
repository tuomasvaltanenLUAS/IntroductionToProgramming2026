print("Start!")

# in while-loops, we have to take care of
# the counter variable by ourselves
counter = 1

while counter <= 10:
    print(f"Cycle: {counter}")

    # YOU HAVE TO INCREASE THE COUNTER YOURSELF
    # or otherwise you get an infinite loop
    counter = counter + 1

print("End!")