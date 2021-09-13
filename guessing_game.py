import random

z = input("\nHey! Let's play a number guessing game! Do you want to guess (1), or do you want me to guess (2)?\n")


print("\nGreat! Let's play!!!\n")

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'\nGuess a number between 1 and {x}: '))
        if guess < random_number:
            print("\nSorry, try again. Too low my friend!")
        elif guess > random_number:
            print("\nSorry, try again. Too high my friend!")
        
    print(f"Great job! You guessed it! {random_number} was the target.\n")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"\nIs {guess} too high (h), too low (l), or correct (c)? Answer: ")
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1
    print(f"\nHa, I knew I'd find it! {guess} was the right answer!\n")

if z == "1":
    x = int(input("\nHow many numbers should we include? Numbers: "))
    guess(x)
elif z == "2":
    x = int(input("\nHow many numbers should we include? Numbers: "))
    computer_guess(x)

