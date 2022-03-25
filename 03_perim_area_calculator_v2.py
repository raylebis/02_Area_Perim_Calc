# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Main Routine goes here

# Introduction
print()
print("**** Area Perimeter Calculator ****")
print()

keep_going = ""
while keep_going == "":
    
    width = num_check("Width: ")
    height = num_check("Height: ")
    # Calculates perim (2 x (width + height))
    perimeter = 2 * (width + height)
    # Calculates Area (area x width)
    area = width * height
    # Output area and perim to 2 dp
    print("The area for this quadrilateral is {:.2f} square units".format(area))
    print("The perimeter for this quadrilateral is {:.2f} square units".format(perimeter))
    print()
    keep_going = input("Press <enter> to keep going on any key to quit")
    

print("Thanks for using my area/perimeter calculator")