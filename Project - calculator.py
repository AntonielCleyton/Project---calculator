import time
import os

class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def __init__(self):
        """
        Initializes the Calculator with a default name.
        """
        self.name = 'name'

    def greetings(self):
        """
        Greets the user and asks for their name.
        """
        print('------------------------------')
        print('---Welcome to the calculator!---')
        print('------------------------------')
        self.name = input('Enter your name:\nAnswer: ')

    def clear_screen(self):
        """
        Clears the console screen.
        """
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def new_operation(self):
        """
        Asks the user if they want to perform a new operation.

        Returns:
            int: 1 if the user wants to perform a new operation, 2 if not.
        """
        while True:
            try:
                choice = int(input('Do you want to perform a new operation? 1-YES | 2-NO\nAnswer: '))
                if choice in [1, 2]:
                    return choice
                else:
                    print('Invalid choice. Please choose 1 or 2.')
            except ValueError:
                print('Invalid input. Please enter a number.')

    def operations(self):
        """
        Main method to perform the calculator operations in a loop until the user decides to exit.
        """
        while True:
            try:
                choice = int(input(f'Which operation would you like to perform, {self.name}?\n'
                                   '1 - Addition: +\n'
                                   '2 - Subtraction: -\n'
                                   '3 - Multiplication: *\n'
                                   '4 - Division: /\n'
                                   '5 - Exponentiation: **\n'
                                   '_________\nAnswer: '))

                if choice in [1, 2, 3, 4, 5]:
                    number1 = float(input('Enter the first number: '))
                    number2 = float(input('Enter the second number: '))

                    if choice == 1:
                        result = number1 + number2
                        operation = 'Addition'
                    elif choice == 2:
                        result = number1 - number2
                        operation = 'Subtraction'
                    elif choice == 3:
                        result = number1 * number2
                        operation = 'Multiplication'
                    elif choice == 4:
                        if number2 != 0:
                            result = number1 / number2
                            operation = 'Division'
                        else:
                            print('Error: Division by zero is not allowed.')
                            continue
                    elif choice == 5:
                        result = number1 ** number2
                        operation = 'Exponentiation'

                    print(f'Result of {operation}: {result}')
                else:
                    print(f'{self.name}, you made an invalid choice! Please choose one of the options below.')

                if self.new_operation() == 1:
                    print(f'Okay, {self.name}! Clearing screen...')
                    self.clear_screen()
                    continue
                else:
                    print(f'Exiting the system! See you soon, {self.name}!')
                    break
            except ValueError:
                print('Invalid input. Please enter a number.')

if __name__ == "__main__":
    # Create an instance of the Calculator class and start the interaction
    calculator = Calculator()
    calculator.greetings()
    calculator.operations()
