# checks that users enter a number that is more than zero
valid = False
while not valid:
    # ask user to enter a number
    response = float(input("Enter a number: "))

    # checks number is more than zero
    if response > 0:
        valid = True
    # outputs error if input is invalid
    else:
        print("Please enter a number that is more than zero.")
        print()