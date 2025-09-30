import random

def play_game():
    number = random.randint(1, 100)  # secret number
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))#Gets user input for the guess
            attempts += 1 # increment attempts of the user input

            if guess < number:
                print("Too low! Try again.") # if the guess is lower than the number
            elif guess > number:
                print("Too high! Try again.") # if the guess is higher than the number
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.") 
                return attempts  # return score when correct
        except ValueError:
            print("⚠️ Please enter a valid number.") # handle non-integer inputs
            continue

def main():
    scores = [] # list to keep track of scores

    while True:
        score = play_game() # play the game and get the score
        scores.append(score) # add score to the list
        print(f"Best score so far: {min(scores)} attempts")

        again = input("Play again? (y/n): ").lower() # ask user if they want to play again
        if again != "y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__": # run the main function
    main()
