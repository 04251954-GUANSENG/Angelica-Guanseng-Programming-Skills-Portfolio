# Exercise 5: Days of the Month (With Advanced Requirements)

months = { # dictionary storing month numbers as keys and tuples of month name and days as values
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

# prints a welcome message introducing the tool
print("\nWelcome! This tool provides the number of days in any month of the year.")

while True: # loop that asks if the user wants to start using the tool
    confirm = input("Would you like to continue? (yes/no): ").strip().lower()

    if confirm == "yes": # checks if user wants to continue
        while True: # loop that keeps asking for a valid month number
            month_input = input("\nEnter the month number (1-12): ").strip() 

            if month_input.isdigit(): # checks if the input is a number
                month = int(month_input) # converts the input to an integer
                if 1 <= month <= 12: # checks if the number corresponds to a valid month
                    name, days = months[month] # retrieves the month name and number of days

                    if month == 2: # special handling for february
                        while True: # loop to handle leap year input
                            leap = input("Is it a leap year? (yes/no): ").strip().lower()
                            if leap == "yes": # if it is a leap year
                                print(f'\n{name} has 29 days.\n')
                                break # exits the leap year loop
                            elif leap == "no": # if it is not a leap year
                                print(f'\n{name} has {days} days.\n')
                                break # exits the leap year loop
                            else: # invalid input handling
                                print("\nInvalid input. Please type 'yes' or 'no'.")
                    
                    else: # handles all other months
                        print(f'\n{name} has {days} days.\n')
                    
                    while True: # loop asking if user wants to use the tool again
                        again = input("Would you like to use the tool again? (yes/no): ").strip().lower()
                        if again == "yes": # if yes, break to outer loop to start again
                            break # exits use-again loop to start over
                        elif again == "no": # if no, exit the program
                            print("\nThank you for using the Days of the Month tool. Goodbye!\n")
                            exit() # stops program execution
                        else: # stops program execution
                            print("Invalid input. Please type 'yes' or 'no'.\n")

                else: # input number is not a valid month
                    print("Invalid month number. Please enter a number between 1 and 12.")
            else: # input is not numeric
                print("Invalid input. Please enter a number.")
        
    elif confirm == "no": # user does not want to start the tool
        print("\nNo worries! Have a nice day. :)\n")
        break # exits the main loop

    else: # invalid input handling for starting the tool
        print("Invalid input. Please type 'yes' or 'no'.\n")