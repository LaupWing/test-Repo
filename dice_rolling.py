from random import randrange

def getRandomNumber(begin, end):
    return randrange(begin, end+1)

flag = True
guess = getRandomNumber(0, 6)

while flag:
    try:
        userInput = int(input("Your Number Guess: "))
        if userInput == int(guess):
            flag = False
            print(f'you got it! {guess}')
    except ValueError:
        print('Not a valid number try again plz')