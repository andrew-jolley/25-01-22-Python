villains = ["The Joker","Magneto","Red Mist","Doc Ock"]
wages = ["21", "17", "3", "5"]

for score in villains:
    for money in wages:
        print(score + money)

for counter in villains:
    print(villains[counter],": £",wages[counter]," million")
