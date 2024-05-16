import time  # Import the time library to use the sleep function
import os  # Import the os library to use the system function

# Define the Calculator class
class Calculator:
    def __init__(self):
        self.name = 'name'  # Initialize the name variable

    # Method to display greetings and ask for the user's name
    def greetings(self):
        print('------------------------------')
        print('---Welcome to the calculator!---')
        print('------------------------------')
        self.name = str(input('Enter your name:\nAnswer: '))  # Ask for the user's name

    # Method to perform mathematical operations
    def operations(self):
        while True:  # Infinite loop to allow multiple operations
            choice = int(input(f'What operation would you like to perform {self.name}:\n1 - Addition: +\n2 - Subtraction: -\n3 - Multiplication: *\n4 - Division: /\n5 - Exponentiation: **\n_________\nAnswer: '))
            if choice == 1:  # Addition
                number1 = int(input('Enter the first number: '))
                number2 = int(input('Enter the second number: '))
                addition = number1 + number2
                print(f'Result: {addition}')
                new_or_exit = int(input('Would you like to perform a new operation? 1-YES | 2-NO\nAnswer: '))
                if new_or_exit == 1:
                    print(f'Okay {self.name}! Clearing screen...')
                    time.sleep(1)
                    os.system('cls')  # Clear the screen (Windows)
                    continue
                else:
                    print(f'Exiting the system! See you soon {self.name}')
                    time.sleep(1)
                    break
            elif choice == 2:  # Subtraction
                number1 = int(input('Enter the first number: '))
                number2 = int(input('Enter the second number: '))
                subtraction = number1 - number2
                print(f'Result: {subtraction}')
                new_or_exit = int(input('Would you like to perform a new operation? 1-YES | 2-NO\nAnswer: '))
                if new_or_exit == 1:
                    print(f'Okay {self.name}! Clearing screen...')
                    time.sleep(1)
                    os.system('cls')
                else:
                    print(f'Exiting the system! See you soon {self.name}')
                    time.sleep(1)
                    break
            elif choice == 3:  # Multiplication
                number1 = int(input('Enter the first number: '))
                number2 = int(input('Enter the second number: '))
                multiplication = number1 * number2
                print(f'Result: {multiplication}')
                new_or_exit = int(input('Would you like to perform a new operation? 1-YES | 2-NO\nAnswer: '))
                if new_or_exit == 1:
                    print(f'Okay {self.name}! Clearing screen...')
                    time.sleep(1)
                    os.system('cls')
                else:
                    print(f'Exiting the system! See you soon {self.name}')
                    time.sleep(1)
                    break
            elif choice == 4:  # Division
                number1 = int(input('Enter the first number: '))
                number2 = int(input('Enter the second number: '))
                division = number1 / number2
                print(f'Result: {division}')
                new_or_exit = int(input('Would you like to perform a new operation? 1-YES | 2-NO\nAnswer: '))
                if new_or_exit == 1:
                    print(f'Okay {self.name}! Clearing screen...')
                    time.sleep(1)
                    os.system('cls')
                else:
                    print(f'Exiting the system! See you soon {self.name}!')
                    time.sleep(1)
                    break
            elif choice == 5:  # Exponentiation
                number1 = int(input('Enter the first number: '))
                number2 = int(input('Enter the second number: '))
                exponentiation = number1 ** number2
                print(f'Result: {exponentiation}')
                new_or_exit = int(input('Would you like to perform a new operation? 1-YES | 2-NO\nAnswer: '))
                if new_or_exit == 1:
                    print(f'Okay {self.name}! Clearing screen...')
                    time.sleep(1)
                    continue
                else:
                    print(f'Exiting the system! See you soon {self.name}!')
                    time.sleep(1)
                    break
            else:  # If the user makes an invalid choice
                print(f'{self.name}, you made an invalid choice! Please choose from the options below:')
                print('-----------------------------')
                new_or_exit = int(input('Would you like to perform a new operation? 1-YES | 2-NO\nAnswer: '))
                if new_or_exit == 1:
                    print(f'Okay {self.name}! Clearing the screen...')
                    time.sleep(1)
                    continue
                elif new_or_exit == 2:
                    print(f'Exiting the system! See you soon {self.name}!')
                    time.sleep(1)
                    break
                else:
                    print(f'You made another wrong choice {self.name}...')
                    print(f'Ending program. Restart it if you want to perform another operation {self.name}')
                    time.sleep(2)
                    break

# Initialize the calculator and call the methods
starting = Calculator()
starting.greetings()
starting.operations()
