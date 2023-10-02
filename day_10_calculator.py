'''A simple calculator to do basic maths'''

logo = """
 _____________________
|  _________________  |
| | VandyCalc    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# calculation functions
def add(n1, n2):
    return (n1 + n2)

def subtract(n1, n2):
    return (n1 - n2)

def multiply(n1, n2):
    return (n1 * n2)

def divide(n1, n2):
    return (n1 / n2)

# dictionary of operations
operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}

# print operation options, retrieve desired operation
def select_operation():
    print("Operations:", end = " ")
    for item in operations.keys():
        print(item, end = " ")
    return input("\nChoose an operation: ")

# pass user input to appropriate function, compute answer
def compute_answer(num1, operation_choice, num2):
    operation = operations[operation_choice]
    result = operation(num1, num2)
    print(f"{num1} {operation_choice} {num2} = {result}")
    return result

# main calculator operation by calling above functions, also offer continued 
# operation, or restarting
def calculator():
    print(logo)
    num1 = float(input("\nWhat's the first number? "))
    operation_choice = select_operation()
    num2 = float(input("What's the second number? "))
    answer = compute_answer(num1, operation_choice, num2)

    # offer another operation, compute if yes
    while True:
        user_continue = input("Continue computing with this result (Y/N)? ").upper()
        if user_continue == "Y":
            num1 = answer
            print(f"\nFirst number is {num1}")
            new_operation_choice = select_operation()
            new_num2 = float(input("What's the second number? "))
            answer = compute_answer(num1, new_operation_choice, new_num2)
    # if no continued operation, offer restart
        elif user_continue == "N":
            start_over = input("\nStart a new calculation (Y/N): ").upper()
            if start_over == "Y":
                calculator()
            elif start_over == "N":
                print("Thanks for the tasty numbers, have a great day!")
                break

if __name__ == "__main__":
    calculator()