def calcDouble(amount):
	amount = 2 * amount
	return amount
def calcHalf(amount):
	amount = amount / 2
	return amount
def calcTenMore(amount):
	amount = 10+  amount
	return amount
question = 120
answer = calcDouble(question)
print("Double",question,"is",answer)
answer = calcHalf(question)
print("Half",question,"is",answer)
answer = calcTenMore(question)
print("Ten more",question,"is",answer)

