import random

# generate random number


# Set up guesses and attempts
max_guesses = 10
guesses_taken = 0

#Have user choose which mode they want to play
user_mode = int(input("Press '1' for easy mode, and '2' for hard mode. "))

# easy mode
if user_mode == 1:
    lucky_number = random.randint(1,10)
    # Start Game loop
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

#hard mode
if user_mode == 2:
    lucky_number = random.randint(1,100)
    # Start Game loop
    while guesses_taken < max_guesses:
        try:
            # Get user's guess
            guess = int(input("Guess a number between 1 and 100. \n"))
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
        if guess != lucky_number and guesses_taken == 10:
            print(f"You ran out of guesses! Game over.")