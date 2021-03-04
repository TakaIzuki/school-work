# Imports



# Functions

# Main execution of the program.
def main():
    # Open provided CSV file
    f = open("Python/airport-project/Airports.txt", 'r')
    # Define list to store seperated CSV file in.
    airports_list = []

    # Loop through file and split each line into seperate lists.
    for i in f:
        split_line = i.split(',')
        # Delete the unneeded newline (\n) from the list
        del split_line[-1]
        # Append the split lines into one list to create a listed version of our CSV file.
        airports_list.append(split_line)

    menu(airports_list)

# Kills program when called.
def exitProgram():
    exit()

# Command line option menu.
def menu(airports_list):
    while True:
        choice = input(
            '''
Choose an option by typing the respective number:
    1 - Enter airport details
    2 - Enter flight details
    3 - Enter price plan and calculate profit
    4 - Clear data
    5 - Quit
            '''
        )

        if choice == '1':
            print("Enter airport details")
        elif choice == '2':
            print("Enter flight details")
        elif choice == '3':
            print("Enter price plan and calculate profit")
        elif choice == '4':
            print("Clear Data")
        elif choice == '5':
            exitProgram()
        else:
            print("Please enter a valid number.")

main()