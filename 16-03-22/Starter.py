totalScore = 0
numScore = 0
goes = 0
moreScores = True
while moreScores:
    score = int(input("Enter the next score, -1 to end: "))
    print('\n')
    totalScore = score + totalScore
    goes += 1
    if score == -1:
        finalScore = int(totalScore) / int(goes)
        finalScore = round(finalScore,0)
        print("Your final average score is: " + str(finalScore))
        print('\n')
        moreScores = False
