from random import randint

goes = int(input("How many goes would you like to play? "))
print('\n')
x = 0
heads = 0
tails = 0

while x != goes:
    currentGo = randint(1,2)
    if currentGo == 1:
        print("Heads")
        print('\n')
        heads += 1
    elif currentGo == 2:
        print("Tails")
        print('\n')
        tails += 1
    x += 1
    
print("You had " + str(heads) + " heads")
print("You had " + str(tails) + " tails")
