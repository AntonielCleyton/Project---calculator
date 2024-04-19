# Welcome message
print("Welcome to the Calculator!")
print("=======================")
print("\n")
print("Choose the type of operation you want to perform: ")
print("===========================================")

# Importing the os module for clearing the console screen
import os

# Variable to control the loop
continue_calculation = True

while continue_calculation:
    # User input for selecting the operation
    operation = int(input("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Exponentiation\n"))

    print("===========================================")

    # Performing the selected operation
    if operation == 1:
        # Addition operation
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        calculation = number_1 + number_2
        print("___________________")
        print("The sum of {} and {} is: {}".format(number_1, number_2, calculation))
        print("___________________")
        choice = int(input("Do you want to perform another operation? 1 - YES or 2 - NO\n"))
        if choice == 2:
            continue_calculation = False
        os.system('cls')  # Clearing the console screen
    elif operation == 2:
        # Subtraction operation
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        calculation = number_1 - number_2
        print("___________________")
        print("The subtraction of {} from {} is: {}".format(number_2, number_1, calculation))
        choice = int(input("Do you want to perform another operation? 1 - YES or 2 - NO\n"))
        if choice == 2:
            continue_calculation = False
        os.system('cls')
    elif operation == 3:
        # Multiplication operation
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        calculation = number_1 * number_2
        print("___________________")
        print("The multiplication of {} and {} is: {}".format(number_1, number_2, calculation))
        choice = int(input("Do you want to perform another operation? 1 - YES or 2 - NO\n"))
        if choice == 2:
            continue_calculation = False
        os.system('cls')
    elif operation == 4:
        # Division operation
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        calculation = number_1 / number_2
        print("___________________")
        print("The division of {} by {} is: {}".format(number_1, number_2, calculation))
        choice = int(input("Do you want to perform another operation? 1 - YES or 2 - NO\n"))
        if choice == 2:
            continue_calculation = False
        os.system('cls')
    elif operation == 5:
        # Exponentiation operation
        number_1 = int(input("Enter the base number: "))
        number_2 = int(input("Enter the exponent: "))
        calculation = number_1 ** number_2
        print("___________________")
        print("The result of {} raised to the power of {} is: {}".format(number_1, number_2, calculation))
        choice = int(input("Do you want to perform another operation? 1 - YES or 2 - NO\n"))
        if choice == 2:
            continue_calculation = False
        os.system('cls')

# End of the calculator
print("Calculator closed!")
