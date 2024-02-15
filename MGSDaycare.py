"""MGS Daycare program that will be used by a child day-care centre.
It will keep track of children throughout the day. There will be many
features in the program, but we will take it a step at a time and build each
one in turn."""

# Initialize list to keep track of checked-in children
checked_in_children = []


# Function to check a child in
def check_in_child():
    name = input("Enter the name of the child to check in: ")
    checked_in_children.append(name)
    print(name, "has been checked in.")


# Function to check a child out
def check_out_child():
    name = input("Enter the name of the child to check out: ")
    if name in checked_in_children:
        checked_in_children.remove(name)
        print(name, "has been checked out.")
    else:
        print("Error: Child not found in the check-in list.")


# Function to calculate charges
def calculate_charges():
    num_checked_out = int(input("Enter the number of children checked out: "))
    hours = int(input("Enter the number of hours to charge: "))
    total_charge = num_checked_out * 12 * hours
    print("Total charge for", num_checked_out, "children for", hours,
          "hours is $", total_charge)


# Function to print list of checked-in children
def print_checked_in_children():
    print("List of checked-in children:")
    for child in checked_in_children:
        print(child)


print("Welcome to MGS Childcare")
# Main loop
choice = 0
while choice != 5:
    print("___________________________________________________________")
    print("What would you like to do? Please choose one of items below")
    print("___________________________________________________________")
    print()
    print("1. Drop off a Child")
    print("2. Pick up a child")
    print("3. Calculate Costs")
    print("4. Print roll")
    print("5. Exit System")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        check_in_child()
    elif choice == 2:
        check_out_child()
        pass
    elif choice == 3:
        calculate_charges()
        pass
    elif choice == 4:
        print_checked_in_children()
        pass
    elif choice == 5:
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
