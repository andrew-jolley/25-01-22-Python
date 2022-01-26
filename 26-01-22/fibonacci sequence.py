noTerms = 10
#noTerms = int(input("How many terms? "))

num1, num2 = 0, 1
goes = 0
print("Fibonacci sequence:")
while goes < noTerms:
   print(num1)
   nTHTRM = num1 + num2
   num1 = num2
   num2 = nTHTRM
   goes += 1
