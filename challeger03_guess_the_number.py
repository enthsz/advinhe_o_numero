import random  # Import the random module to generate random numbers

# Create a list of numbers from 1 to 50
list_of_number = list(range(1, 51))

# Choose a random number from the list
random_choice = random.choice(list_of_number)

# Print the random number (for debugging)
print(random_choice)

# Initialize variables
guess_count = 5  # Number of guess attempts allowed
guess_limit = 0  # The limit of guess attempts
game_over = False  # Flag to track if the game is over

# Start the game loop
while not game_over:
    print("Find the hidden number of 1 to 50")  # Prompt the user to guess the hidden number

    user_input = int(input("Digit a number: "))  # Get the user's guess as an integer

    # Check if the user's guess is equal to the random number
    if user_input == random_choice:
        game_over = True  # If correct, end the game
        print("You Won")  # Display a winning message
    else:
        guess_count -= 1  # Decrement the number of remaining attempts
        print(f"Wrong! You still have {guess_count} attempts")  # Display remaining attempts

        # Check if the user's guess is higher or lower than the random number
        if user_input > random_choice:
            print("You've passed the number")  # User guessed a number higher than the random number
        else:
            print("Try a bigger number")  # User guessed a number lower than the random number

    # Check if the user has run out of attempts
    if guess_count == guess_limit:
        game_over = True  # If no more attempts left, end the game
        print(f"How pitty the number is {random_choice}")  # Display the correct number

    if game_over:
        play_again = input("Do you want to play again? yes/no: ").lower()  # Ask if the user wants to play again
        if play_again != "yes":  # If the user doesn't want to play again
            break  # Exit the game loop
        else:
            random_choice = random.choice(list_of_number)  # Choose a new random number
            guess_count = 5  # Reset the number of attempts
            guess_limit = 0  # Reset the limit
            game_over = False  # Reset the game flag to start a new game
