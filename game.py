"""A number-guessing game."""

# Put your code here
import random
name = input('What is your name?')
print(f"{name}, I'm thinking of a number between 1 and 100. Try to guess my number.")

def play_game():
    number = random.randint(1,101)
    guess = None
    tries = 0
    too_low = 0
    too_high = 101
   
    while number != guess:
        guess = int(input('Your guess?'))
        if number > guess:
            tries += 1
            print('Your guess is too low, try again')
        elif number < guess:
            tries += 1
            print('Your guess is too high, try again')
        else:
            number == guess
            print(f'Well done, {name}, you found my number in', tries, 'tries.')
            break
    

play_game()
