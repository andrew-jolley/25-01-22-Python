goAgain = ("False")
personA = 0
personB = 0
personC = 0
username = 'admin'
password = 'Password'
login = ("False")

while login != 'True':
    userEnter = input("Please enter the administrator username: ")
    if userEnter == username:
        userPass = input("Please enter the administrator password: ")
        if userPass == password:
            poltA = input("Enter the first candidate: ")
            poltB = input("Enter the second candidate: ")
            poltC = input("Enter the third candidate: ")
            break

        else:
            exit()
    else:
        exit()
while goAgain != 'True':
    print("Enter your vote here")
    vote = input("Enter \'A\' for person A, \'B\' for person B or \'C\' for person C: ")
    if vote == 'A' or vote == 'a':
        print("You voted for " + poltA)
        personA += 1
        print("\n")
    elif vote == 'B' or vote == 'b':
        print("You voted for " + poltB)
        personB += 1
        print("\n")
    elif vote == 'C' or vote == 'c':
        print("You voted for " + poltC)
        personC += 1
        print("\n")
    elif vote == 'Logout':
        login == 'False'
    elif vote == 'END':
        print(poltA + " has " + str(personA) + " votes")
        print(poltB + " has " + str(personB) + " votes")
        print(poltC + " has " + str(personC) + " votes")
        totalVotes = personA + personB + personC
        print("There are " + str(totalVotes)+ " in total")
        break
else:
    exit()
