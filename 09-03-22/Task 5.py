import random

def chooseASuit(number):
    if number == 1:
        suit = "Hearts"
    elif number == 2:
        suit = "Diamonds"
    elif number == 3:
        suit = "Clubs"
    elif number == 4:
        suit = "Spades"
    return suit

def chooseAValue(number):
    if number == 11:
        value = "Jack"
    elif number == 12:
        value = "Queen"
    elif number == 13:
        value = "King"
    elif number == 1:
        value = "Ace"
    else:
        value = number
    return value

for counter in range(10):
    randomNum = random.randint(1,4)
    suit = chooseASuit(randomNum)

    randomNum = random.randint(1,13)
    value = chooseAValue(randomNum)

    print("Your card is the",value,"of",suit)
