file = open("File-1.txt", "a+")
newCountry = input("Enter a new country: ")
file.write(newCountry + "\n")

file.close()

file = open("File-1.txt", "r+")
print(file.read())
