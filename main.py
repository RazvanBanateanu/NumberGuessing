import random

limit = input("Type a number to set a range: ")

if limit.isdigit():
    limit = int(limit)

    if limit <= 0:
        print('Please type a number greater than 0.')
        quit()
else:
    print('Please type a number.')
    quit()

random_number = random.randint(0, limit)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number.')
        continue

    if user_guess == random_number:
        print("This is the secret number!")
        break
    elif user_guess > random_number:
        print("Plese type a lower number!")
    else:
        print("Plese type a higher number!")

print("You found the number in", guesses, "guesses")