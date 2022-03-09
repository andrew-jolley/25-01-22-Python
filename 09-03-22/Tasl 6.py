yes = input("Enter your answer: ")
def answerYorN():
    YorN = yes
    while YorN != 'Y' or YorN != 'y' or YorN != 'N' or YorN != 'n':
        YorN = input("Enter your answer: ")
    else:
        print(YorN)

answerYorN()
