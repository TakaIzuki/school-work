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
def exitProgram(running):
    running = False
    exit()

# Command line option menu.
def menu(airports_list):
    running = True
    while running == True:
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
            continue
        elif choice == '2':
            continue
        elif choice == '3':
            continue
        elif choice == '4':
            continue
        elif choice == '5':
            exitProgram(running)
        else:
            print("Please enter a valid number.")

main()