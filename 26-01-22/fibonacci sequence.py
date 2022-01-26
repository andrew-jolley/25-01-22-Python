noTerms = 10
#noTerms = int(input("How many terms? "))

num1, num2 = 0, 1
count = 0

if noTerms <= 0:
   print("Please enter a positive integer")
elif noTerms == 1:
   print("Fibonacci sequence upto",noTerms,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while count < noTerms:
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1
