def go():
    print("What is the starting unit?")
    start = input("Enter \'KB\' for Kilobytes, \'MB\' for Megabytes \'GB\' for Gigabytes or \'TB\' for Terabytes or \'PB\' for Petabytes: ")

    print("What would you like convert to?")
    end = input("Enter \'KB\' for Kilobytes, \'MB\' for Megabytes \'GB\' for Gigabytes or \'TB\' for Terabytes or \'PB\' for Petabytes: ")

    input1 = float(input("Enter your number: "))

    if start == 'KB' and end == 'MB':
        input1 = input1 / 1000
        print(str(input1) + end)
    elif start == 'MB' and end == 'KB':
        input1 = input1 * 1000
        print(str(input1) + end)
    elif start == 'MB' and end == 'GB':
        input1 = input1 / 1000
        print(str(input1) + end)
    elif start == 'GB' and end == 'MB':
        input1 = input1 * 1000
        print(str(input1) + end)
    elif start == 'GB' and end == 'TB':
        input1 = input1 / 1000
        print(str(input1) + end)
    elif start == 'TB' and end == 'GB':
        input1 = input1 * 1000
        print(str(input1) + end)
    elif start == 'GB' and end == 'PB':
        input1 = input1 / 1000
        print(str(input1) + end)
    elif start == 'PB' and end == 'TB':
        input1 = input1 * 1000
        print(str(input1) + end)
    elif start == 'KB' and end == 'GB':
        input1 = input1 / 1000000
        print(str(input1) + end)
    elif start == 'GB' and end == 'KB':
        input1 = input1 * 1000000
        print(str(input1) + end)
    elif start == 'KB' and end == 'TB':
        input1 = input1 / 1000000000
        print(str(input1) + end)
    elif start == 'TB' and end == 'KB':
        input1 = input1 * 1000000000
        print(str(input1) + end)
    elif start == 'KB' and end == 'PB':
        input1 = input1 / 1000000000000
        print(str(input1) + end)
    elif start == 'PB' and end == 'KB':
        input1 = input1 * 1000000000000
        print(str(input1) + end)
    elif start == 'MB' and end == 'PB':
        input1 = input1 / 1000000000000
        print(str(input1) + end)
    elif start == 'PB' and end == 'MB':
        input1 = input1 * 1000000000
        print(str(input1) + end)

    else:
        print(input1 + start)


print("Welcome to data converter")
input("Press \'Enter\' to start ")
go()
print("Would you like to play again?")
again = input("Enter \'Y\' for Yes and \'N\' for No: ")
if again == 'y' or again == 'Y':
    go()
else:
    exit()
