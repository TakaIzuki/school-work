# Imports



# Functions

# Main execution of the program.
def main():
    # Open provided CSV file
    f = open("Python/airport-project/Airports.txt", "r")
    # Define list to store seperated CSV file in.
    airports_list = []

    # Loop through file and split each line into seperate lists.
    for i in f:
        split_line = i.split(",")
        # Append the seperate lists into one list to create a listed version of our CSV file.
        airports_list.append(split_line)

    print(airports_list)

# Kill program when called
def exitProgram():
    exit()

# Command line option menu
def menu():
    print(
        '''
Choose an option by typing the respective number:
    1 - 
    2 - 
    3 -
    4 -
        '''
    )

main()