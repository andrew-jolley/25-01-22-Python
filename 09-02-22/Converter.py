print("What is the starting unit?")
start = input("Enter \'TB\' for Terabytes or \'GB\' for Gigabytes: ")

print("What would you like convert to?")
end = input("Enter \'TB\' for Terabytes or \'GB\' for Gigabytes: ")

input1 = float(input("Enter your number: "))

if start == 'TB' and end == 'GB':
    input1 = input1 * 1000
    print(str(input1) + end)
elif start == 'GB' and end == 'TB':
    input1 = input1 / 1000
    print(str(input1) + end)
else:
    print(input1 + start)
