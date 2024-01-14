import random

#Function to generate a random number between 1 and 100
def get_random_number():
    return random.randint(1, 100)

#Function to take user input for guesses
def get_guess():
    while True:
        try:
            guess = int(input('Enter your guess: '))
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100")
            return guess
        except ValueError as e:
            print(e)

#Function to check if the user has guessed correctly
def is_correct(guess, number):
    return guess == number

#Function to play the game
def play():
    random_number = get_random_number()
    while True:
        guess = get_guess()
        if is_correct(guess, random_number):
            print('Congratulations! You guessed correctly.')
            break
        else:
            if guess < random_number:
                print('Too low. Try again.')
            else:
                print('Too high. Try again.')
    return

#Start the game loop
play()





