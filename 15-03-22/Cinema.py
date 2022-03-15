red = 100
black = 250
yellow = 1500

redSold = input("How many seats sold for Red Screen? ")
blackSold = input("How many seats sold for Black Screen? ")
yellowSold = input("How many seats sold for Yellow Screen? ")

redLeft = int(red) - int(redSold)
blackLeft = int(black) - int(blackSold)
yellowLeft = int(yellow) - int(yellowSold)


if redLeft < 0 or blackLeft < 0 or yellowLeft < 0:
    print("Error")
else:
    print("Red: " + str(redLeft) + " seats remaining ")
    print("Black: " + str(blackLeft) + " seats remaining ")
    print("Yellow: " + str(yellowLeft)+ " seats remaining ")
