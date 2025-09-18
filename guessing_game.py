import random

# generate random number
lucky_number = random.randint(1,10)

# Set up guesses and attempts
max_guesses = 5
guesses_taken = 0

# Start Game loop
try:
    while guesses_taken < max_guesses:
        try:
            # Get user's guess
            guess = int(input("Guess a number between 1 and 10. \n"))
        except:
            print("Invalid input. Please enter a number.")
            continue
        
        guesses_taken += 1

        # Checks for a win
        if guess < lucky_number:
            print("Too low!")
        elif guess > lucky_number:
            print("Too high!")
        else:
            print(f"Good job! You guessed the lucky number in {guesses_taken} guesses!")
            break

        # If the user runs out of guesses
        if guess != lucky_number and guesses_taken == 5:
            print(f"You ran out of guesses! Game over.")
except KeyboardInterrupt:
    print("Game ended by user.")