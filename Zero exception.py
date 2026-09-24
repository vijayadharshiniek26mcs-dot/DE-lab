try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number : "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error : cannot divide by Zero")
finally:
    print("finally block is executed")
