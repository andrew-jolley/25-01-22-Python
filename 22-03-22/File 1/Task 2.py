file = open("File-2.txt", "w")

name1 = input("What's your name? ")
name2 = input("What's your name? ")
name3 = input("What's your name? ")

file.write(name1 + "\n")
file.write(name2 + "\n")
file.write(name3 + "\n")
file.close()
