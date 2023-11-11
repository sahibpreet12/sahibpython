import random

min_number = 1
max_number = 100

num_guesses = 0  # Define num_guesses in an outer scope

secret_number = random.randrange(0, 101, 5)

print("The Secret number was", secret_number)

def guess_the_number():
    guess = random.randrange(0, 101, 5)
    print("The initial guess was",guess)
    global num_guesses 

    def incrementing_the_guess():
        nonlocal guess
        guess += 5
        global num_guesses
        num_guesses += 1
    def decrementing_the_guess():
        nonlocal guess
        guess -= 5
        global num_guesses
        num_guesses += 1

    while guess != secret_number:
        if guess >= secret_number:
            decrementing_the_guess()
        else:
            incrementing_the_guess()
    if guess == secret_number:
        print("Congratulations! The AI successfully guessed the number in", num_guesses, "guesses")
    else:
        print("Something is wrong")
    print("The final guess was", guess)

guess_the_number()

        