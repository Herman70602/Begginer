

try:
    answer = 10/0
    value = 10/0
    number = int(input("Enter a number "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invald Input")