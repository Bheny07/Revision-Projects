"""MGS Daycare program that will be used by a child day-care centre.
It will keep track of children throughout the day. There will be many
features in the program, but we will take it a step at a time and build each
one in turn."""

# Initialize list to keep track of checked-in children
checked_in_children = []

choice = 0
while choice != 5:
    print("____________")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of items below")
    print("____________")
    print()
    print("1. Drop off a Child")
    print("2. Pick up a child")
    print("3. Calculate Costs")
    print("4. Print roll")
    print("5. Exit System")
    print()
    choice = int(input("Enter your choice (number between 1 and 5):"))
    print()

    if choice == 1:
        def check_in_child():
            name = input("Enter the name of the child to check in: ")
            checked_in_children.append(name)
            print(name, "has been checked in.")

    elif choice == 2:
        pickUp()

    elif choice == 3:
        calcCost()

    elif choice == 4:
        printRoll()

    else:
        print("Goodbye")


