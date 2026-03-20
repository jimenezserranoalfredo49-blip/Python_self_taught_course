# exceptions = an event that interrupts the flow of a program
#           (ZeroDivisionError, TypeError, ValueError)
# Recommended usage when code could lead to errors, like input
# 1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number:"))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please insert a whole number")
finally:
    print("Do some cleanup")