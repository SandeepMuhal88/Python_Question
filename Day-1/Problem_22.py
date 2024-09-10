import random

def play_game():
    number_of_guess_left = 3
    random_number = random.randint(0, 10)

    while number_of_guess_left > 0:
        guess = int(input("Enter your numerical guess: "))
        if guess != random_number:
            number_of_guess_left -= 1
            print(f"Incorrect guess. You have {number_of_guess_left} guesses left.")
        else:
            print("Congratulations! You guessed the number correctly.")
            break
    else:
        print("You lose! You've used up all your guesses.")

play_game()