# Exercise 6: Brute Force Attack (With Advanced Requirements)

password = "12345" # correct password for verification
max_attempts = 5 # maximum number of allowed attempts
attempts_left = max_attempts # tracks how many attempts remain
first_incorrect = True # flag to check if it's the user's first incorrect attempt

# asks user for their name and displays warning messages
name = input("\nState your name: ")
print("\nNOTICE: This system is actively monitored. Unauthorized access is a criminal offense.")
print(f'All access attempts are logged and will be traced. You have {max_attempts} attempts.')

while attempts_left > 0: # loop continues while user still has attempts left
    attempt = input("\nEnter password: ")

    if attempt == password: # checks if entered password is correct
        print(f'Credentials verified. Access granted to {name}. Proceed with authorized actions only.\n')
        break # exits loop once password is correct

    else: # runs when entered password is incorrect
        attempts_left -= 1 # subtracts 1 attempt after incorrect password

        if attempts_left > 0: # checks if there are still attempts left
            if first_incorrect: # checks if it's the user's first wrong attempt
                print(f'Password incorrect. {attempts_left} attempt(s) remaining. Continued failure will trigger account locked.')
                first_incorrect = False # changes flag after first incorrect attempt
            else: # runs for all incorrect attempts after the first
                print(f'Password incorrect. {attempts_left} attempt(s) remaining.')
                
        else: # runs when user has no attempts left
            print("Maximum attempts reached. ACCESS DENIED. Account locked, incident recorded, and authorities have been alerted!!!\n")