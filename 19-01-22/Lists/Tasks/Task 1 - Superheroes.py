heroes = ["Batman","Wonder Woman","Superman","Spiderman"]

print("Current pilot: ",heroes[0])

print("Current co-pilot: ",heroes[1])

heroes.remove("Superman")

heroes.insert(2, "Hit Girl")

sphr1 = input("Enter superhero 1: ")
sphr2 = input("Enter superhero 2: ")

heroes.append(sphr1)
heroes.append(sphr2)

print(heroes)
