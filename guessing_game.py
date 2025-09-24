import random

#Have user choose which mode they want to play
user_mode = int(input("Press '1' for easy mode, '2' for hard mode, and '3' for impossible mode. \n"
                      "easy mode = 10 guesses, hard mode = 5 guesses, impossible mode = 3 guesses "))

def main():
    if user_mode == 1:
        easy_mode()
    elif user_mode == 2:
        hard_mode()
    elif user_mode == 3:
        impossible_mode()
    else:
        print("Invalid input. Try again!")

# easy mode
def easy_mode():
    lucky_number = random.randint(1,10)
    max_guesses = 10    
    guesses_taken = 0
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
        elif guess == lucky_number:
            print(f"Good job! You guessed the lucky number in {guesses_taken} guesses!")
            play_again = input("Would you like to play again? If so press the 'a' key and enter. If not press 'q'. ")
            if play_again == 'a':
                main()
            elif play_again == 'q':
                break
            else:
                print("Invalid input. Try again!")

        # If the user runs out of guesses
        if guess != lucky_number and guesses_taken == 10:
            print(f"You ran out of guesses! Game over.")
            play_again = input("Would you like to play again? If so press the 'a' key and enter. If not press 'q'. ")
            if play_again == 'a':
                main()
            elif play_again == 'q':
                break
            else:
                print("Invalid input. Try again!")

#hard mode
def hard_mode():
    lucky_number = random.randint(1,100)
    max_guesses = 5
    guesses_taken = 0
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
        elif guess == lucky_number:
            print(f"Good job! You guessed the lucky number in {guesses_taken} guesses!")
            play_again = input("Would you like to play again? If so press the 'a' key and enter. If not press 'q'. ")
            if play_again == 'a':
                main()
            elif play_again == 'q':
                break
            else:
                print("Invalid input. Try again!")

        # If the user runs out of guesses
        if guess != lucky_number and guesses_taken == 5:
            print(f"You ran out of guesses! Game over.")
            play_again = input("Would you like to play again? If so press the 'a' key and enter. If not press 'q'. ")
            if play_again == 'a':
                main()
            elif play_again == 'q':
                break
            else:
                print("Invalid input. Try again!")

#impossible mode
def impossible_mode():
    lucky_number = random.randint(1,100)
    max_guesses = 3
    guesses_taken = 0
    # Start Game loop
    while guesses_taken < max_guesses:
        try:
            # Get user's guess
            guess = int(input("Guess a number between 1 and 100. \n"))
        except:
            print("Invalid input. Please enter a number.")
            continue
        
        guesses_taken += 1
        if guesses_taken == 1:
            if lucky_number % 2 == 0:
                print("Hint: The lucky number is even!")
            else:
                print("Hint: The lucky number is odd!")
        # Checks for a win
        if guess < lucky_number:
            print("Too low!")
        elif guess > lucky_number:
            print("Too high!")
        elif guess == lucky_number:
            print(f"Good job! You guessed the lucky number in {guesses_taken} guesses!")
            play_again = input("Would you like to play again? If so press the 'a' key and enter. If not press 'q'. ")
            if play_again == 'a':
                main()
            else:
                break

        # If the user runs out of guesses
        if guess != lucky_number and guesses_taken == 3:
            print(f"You ran out of guesses! Game over.")
            play_again = input("Would you like to play again? If so press the 'a' key and enter. If not press 'q'. ")
            if play_again == 'a':
                main()
            elif play_again == 'q':
                break
            else:
                print("Invalid input. Try again!")

main()