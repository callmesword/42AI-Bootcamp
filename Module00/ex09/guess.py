import random
import string



    rng = []
    for i in range(1, 100):
        rng.append(str(i))
    return rng



def guess():
    rng = []
    for i in range(1, 100):
        rng.append(str(i))
        
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
    num = random.randint(1, 99)
    count = 1
    user_guess = input("What's your guess between 1 and 99?\n>> ")
    if user_guess == '42':
        print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!")
        quit()
    else:
        pass
    while user_guess != 'exit' and user_guess >= '1' and user_guess <= '99':
        if user_guess > str(num):
            print("too high")
            user_guess = input("What's your guess between 1 and 99?\n>> ")
            count += 1
        elif user_guess < str(num):
            print("too low")
            user_guess = input("What's your guess between 1 and 99?\n>> ")
            count += 1
        elif user_guess == str(num):
            print("Congratulations, you've got it!\nYou won in {} attempts!".format(count))
            quit()
        elif check_letter(user_guess):
            print("invalid input!")
            user_guess = input("What's your guess between 1 and 99?\n>> ")
            continue

    else:
        if user_guess > '99' or user_guess < '0':
            print("Please enter a number between 1 and 99.")
            user_guess = input("What's your guess between 1 and 99?\n>> ")
        else:
            print("Goodbye!")

guess()