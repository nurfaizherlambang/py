import sys

try:
    x = int(input("x: "))  
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can't divide by zero.")
    sys.exit(1)

print(f"The result is {result}.")