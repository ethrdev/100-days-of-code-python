#### Demo: Calculator
### First try written by ethR
## The goal is to build a calculator program.
# Demo
# https://appbrewery.github.io/python-day10-demo/

from art import logo

print(logo)
## Storing Functions as a Variable Value
# You can store a reference to a function as a value to a variable. e.g.
def add(n1, n2):
    return n1 + n2
        
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8

# In the starting file, you'll see a dictionary that references each of the mathematical calculations that 
# can be performed by our calculator. 
# Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

# TODO Write out the other 3 functions - subtract, multiply and divide.

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

arithmetic_methods = {}
arithmetic_methods["+"] = add
arithmetic_methods["-"] = substract
arithmetic_methods["*"] = multiply
arithmetic_methods["/"] = divide

print(arithmetic_methods)


# TODO Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
print(arithmetic_methods["*"](4, 8))

calc_to_continue = True
number_to_begin_with = 0
result = 0
app_runs = True



### Functionality
while app_runs:
    # Program asks the user to type the first number.
    first_chosen_number = int(input("Please type your first number: "))

    # Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
    chosen_operator = str(input("Choose your operation... '+', '-', '*' or '/': "))

    # Program asks the user to type the second number.
    second_chosen_number = int(input("Please type your second number: "))

    # Program works out the result based on the chosen mathematical operator.
    result = int(arithmetic_methods[chosen_operator](first_chosen_number, second_chosen_number))
    print(result)

    # Program asks if the user wants to continue working with the previous result.
    user_want_to_continue = str(input("Do you want to continue with the privious result? Type 'y' for yes and 'n' for no: "))
    
    if user_want_to_continue == "y" or user_want_to_continue == "yes":
        calc_to_continue = True
        
    # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    while calc_to_continue:
        # Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
        chosen_operator = input("Choose your operation... '+', '-', '*' or '/': ")
        # Program asks the user to type the next number.
        next_chosen_number = int(input("Please type your next number: "))
        result = int(arithmetic_methods[chosen_operator](result, next_chosen_number))
        print(result)
        # Program asks if the user wants to continue working with the previous result.
        user_want_to_continue = str(input("Do you want to continue with the previous result? Type 'y' for yes and 'n' for no: "))
    
        # If no, program asks the user for the fist number again and wipes all memory of previous calculations.
        if user_want_to_continue == "n" or user_want_to_continue == "no":
                calc_to_continue = False
            
