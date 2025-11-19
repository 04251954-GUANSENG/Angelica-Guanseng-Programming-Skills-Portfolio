# Exercise 8: Simple Search (With Advanced Requirements)

list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # list of suspects

# prints the scenario and displays the suspect list
print("\nCOOKIE THEIF ALERT! A cookie has been stolen from the cookie jar!")
print("\nOBJECTIVE: Identify the culprit in the list of suspects.")
print("Suspect List:", list)

list_lower = [name.lower() for name in list] # converts all names to lowercase for easier searching

while True: # loop that keeps asking until thief is found
    search = input("\nEnter the name you want to investigate: ")
    search_clean = search.lower() # converts user input to lowercase

    if search_clean in list_lower: # checks if the entered name exists in the suspect list
        suspect = list[list_lower.index(search_clean)] # finds the original name format

        if search_clean == "sam": # checks if the suspect is Sam (the thief)
            print(f'\n{suspect} WAS FOUND in the list...')
            print("AND HE'S THE COOKIE THIEF!")
            print("Sam, we caught you red-handed!")
            break # exits loop once thief is found
        else: # runs if suspect is found but is not Sam
            print(f'\n{suspect} was found in the list...')
            print(f'but {suspect} isn''t the culprit. Continue your investigation!')
            
    else: # runs when the entered name is not in the list
        print(f'\n{search} is NOT in the list.')
        print("That name isn't registered as a suspect... but nice try.")

# prints final message after finding the thief
print("\nCASE CLOSED! You found the thief and saved the cookie jar!")