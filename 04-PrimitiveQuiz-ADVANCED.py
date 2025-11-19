# Exercise 4: Primitive Quiz (With Advanced Requirements) 

quiz = { # dictionary of countries as keys and their capitals as values
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Croatia": "Zagreb",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "France": "Paris",
    "Germany": "Berlin",
    "Hungary": "Budapest",
    "Italy": "Rome",
    "Kosovo": "Pristina"
}

# prints a welcome message and asks user to enter their name
print("\nWelcome to the Capital Cities of Europe Quiz! Kindly enter your name to start.")
name = input("Enter your name: ")

while True: # loop that repeats quiz prompt until valid input is given
    ready = input(f'\nHello {name}! Are you ready to take the Capitals Cities of Europe Quiz? (yes/no): ').lower()

    if ready == "yes": # checks if user is ready to begin the quiz
        print("Great! Let's start with the quiz.")
        score = 0 # variable to store the number of correct answers

        # loop that goes through each country and its capital
        for country, capital in quiz.items():
            answer = input(f'\nWhat is the capital of {country}? ')

            if answer.lower() == capital.lower(): # checks if user's answer matches the correct capital
                print(f'Correct! {capital} is the capital of {country}.')
                score += 1 # adds 1 point for each correct answer
            else: # executes when user's answer is incorrect
                print(f'Wrong. {capital} is the capital of {country}.')

        # prints final score after completing the quiz
        print(f'\nQuiz complete! You got {score} out of {len(quiz)} correct.\n')
        break # exits the loop after quiz ends
    
    elif ready == "no": # checks if the user is not ready to take the quiz
        print(f'No worries, {name}! Have a nice day. :)\n')
        break # exits the loop if user is not ready

    else: # runs when user enters an invalid response
        print("Invalid response. Please type ""yes"" or ""no"".")