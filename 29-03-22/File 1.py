file = open("File-1.txt" , "w+")

fName = input("What is your first name? ")
lName = input("What is your surname? ")
gend = input("What is your gender? ")
form = input("What is your form? ")

file.write("First name: " + fName + "\n")
file.write("Surname: " + lName + "\n")
file.write("Gender: " + gend + "\n")
file.write("Form: " + form + "\n")

file = open("File-1.txt" , "r+")

print(file.read())

file.close()
