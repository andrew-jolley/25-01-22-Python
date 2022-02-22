from time import sleep

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1, 2, 3 or 4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Addition selected")
            sleep(1)
            print("Processing...")
            sleep(1)
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("Subtraction selected")
            sleep(1)
            print("Processing...")
            sleep(1)
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("Multiplication selected")
            sleep(1)
            print("Processing...")
            sleep(1)
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("Division selected")
            sleep(1)
            print("Processing...")
            sleep(1)
            print(num1, "/", num2, "=", divide(num1, num2))
            
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
