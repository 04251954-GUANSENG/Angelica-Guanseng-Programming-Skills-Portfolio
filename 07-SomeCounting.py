# Exercise 7: Some Counting

print("\nWelcome! This tool provides different counting sequences to help you practice number patterns.") # prints a welcome message introducing the tool

while True: # main loop to keep the program running
    confirm = input("Would you like to continue? (yes/no): ").lower()

    if confirm == "yes": # if user wants to continue
        while True: # loop for counting options
            print("\nPlease select a counting option below:") # displays counting options
            print("1 - Count up from 0 to 50.")
            print("2 - Count down from 50 to 0.")
            print("3 - Count down from 30 to 50.")
            print("4 - Count down from 50 to 10 by 2s.")
            print("5 - Count up from 100 to 200 by 5s.")

            choice = input("\nEnter the number of your choice (1-5): ")

            if choice == "1": # counting option 1
                print("\nCounting up from 0 to 50:")
                for i in range(0, 51, 1): # loop to count from 0 to 50
                    print(i) # prints each number

            elif choice == "2": # counting option 2
                print("\nCounting down from 50 to 0:")
                for i in range(50, -1, -1): # loop to count down from 50 to 0
                    print(i)
    
            elif choice == "3": # counting option 3
                print("\nCounting up from 30 to 50:")
                for i in range(30, 51, 1): # loop to count from 30 to 50
                    print(i)
    
            elif choice == "4": # counting option 4
                print("\nCounting down from 50 to 10 by 2s:")
                for i in range(50, 9, -2): # loop to count down from 50 to 10 by 2s
                    print(i)

            elif choice == "5": # counting option 5
                print("\nCounting up from 100 to 200 by 5s:")
                for i in range(100, 201, 5): # loop to count up from 100 to 200 by 5s
                    print(i)
    
            else: # runs when user enters an invalid choice
                print("Invalid response. Please enter a number between 1 and 5.")
                continue # goes back to asking for a valid counting option

            while True: # loop to ask if user wants to use the tool again after valid counting
                again = input("\nWould you like to use the tool again? (yes/no): ").lower()
                if again == "yes": # if yes, go back to counting options
                    break # exits this loop and returns to counting options
                elif again == "no": # if no, exit the program
                    print("\nThank you for using the Counting tool. Goodbye!\n")
                    exit() # terminates program
                else: # runs if user input is invalid
                    print("Invalid input. Please type 'yes' or 'no'.")
    
    elif confirm == "no": # user does not want to start the tool
        print("\nNo worries! Have a nice day. :)\n")
        break # exits the main loop

    else: # invalid input handling for starting the tool
        print("\nInvalid input. Please type 'yes' or 'no'.")