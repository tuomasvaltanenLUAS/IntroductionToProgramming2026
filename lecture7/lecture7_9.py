print("Start!\n")

# MAIN LOOP -> run this 3 times only
for x in range(3):
    print(f"MAIN LOOP: x = {x}")

    # nested loop -> run this 5 times in every main iteration
    for y in range(5):
        print(f"\t\tnested loop y = {y}")

print("\nEnd!")