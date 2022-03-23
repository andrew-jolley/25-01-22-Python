file = open("File-2.txt" , "w+")

colour1 = input("Enter a colour: ")
colour2 = input("Enter a colour: ")
colour3 = input("Enter a colour: ")

file.write(colour1 + "\n")
file.write(colour2 + "\n")
file.write(colour3 + "\n")

file = open("File-2.txt" , "r+")

print("\n")

print(file.read())

file.close()
