# Exercise 10: Is it even?

def check_even_odd(number): # defines a function that checks if a number is even or odd
    if number % 2 == 0: # checks if the number is divisible by 2
        return (f'{number} is an even number.')
    else: # runs if number is not divisible by 2
        return (f'{number} is an odd number.')

def main(): # defines the main function that runs the tool
    print("\nWelcome! This tool will help you determine if a number is even or odd.")

    while True: # loop to validate if user wants to start using the tool
        use_tool = input("Would you like to continue? (yes/no): ").lower()
        if use_tool == "yes": # if user wants to continue
            break # exit loop and start tool
        elif use_tool == "no": # if user does not want to use the tool
            print("\nNo worries! Have a nice day. :)\n")
            return # exits the program
        else: # if user enters invalid response
            print("Invalid response. Please type 'yes' or 'no'.\n")
    
    while True: # main loop for entering numbers repeatedly
        try: # checks for valid integer input
            num = int(input("\nEnter a number: "))
            result = check_even_odd(num) # calls function to check even or odd
            print(result) # 
        except ValueError: # if input is not an integer
            print("Please enter a valid integer")
            continue # asks for number again
        
        while True: # loop to validate if user wants to use the tool again
            again = input("\nWould you like to use the tool again? (yes/no): ").lower()
            if again == "yes": # if user wants to continue
                break # break this inner loop to ask for a new number
            elif again == "no": # if user wants to stop
                print("\nThank you for using the Even or Odd tool. Goodbye!\n")
                return # exit program
            else: # if user enters invalid response
                print("Invalid input. Please type 'yes' or 'no'.")

# calls main function to start the program
main()