#### Functions with Output

# We've seen functions with only an execution body, functions with inputs that allow for variation in execution of the function 
# body and now we'll see the final form of functions. Functions that can have outputs.

# Syntax
# You can create a function with a body, input and output like this:

'''
def function_name(input_parameter):
    <body of function that uses input_argument>
    return output
'''


# Create a function called format_name() that takes two inputs: f_name and `l_name'.
def format_name(f_name, l_name):
    # Use the title() function to modify the f_name and l_name parameters into Title Case.
    # We are tronsform the input into a title case and when the function is called, it will create an output.
    # The output will be stored in the variables formated_f_name and formated_l_name.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()  
    
    # The formatted string becomes the output of the function.
    return f"{formated_f_name} {formated_l_name}"

# It replaces the part of the code where the function was called.
# format_name(f_name = "etHer", l_name = "DeV") # Ether Dev
formated_string = format_name(f_name = "etHer", l_name = "DeV")    
print(formated_string)
# OR
print(format_name(f_name = "etHer", l_name = "DeV"))  


### Examples of already known functions with output
# The len() function returns the length of an object.
# "Hello" is the input, len is the function
# Once the function is completed, the return will replace the len("Hello") cody by the output of the function.
# The output will get stored in the variable output.
output = len("Hello")

##Print vs. Output
# Return vs. Display: The return statement is used to give back a value from a function, which can be used later, 
# while print is used to display a value to the console only for the programmer to see.

def function_1(text):
    return text + text # "hellohello"

def function_2(text):
    return text.title() # Hello

# Neithe rof these functions have a print statement

# We call the first function and pass in "hello" and save it to an output variable
# output = function_1("hello")
# print(output) # hellohello

# What if we take the output of function_1 and reuse it as an input into function_2?
# The output of function_1 is in fact a string and is a piece of 'text'
# So we can put it in the function_2 as an input

# So now the output of function_1 becomes the input of function_2 and then that input is title-cased
output = function_2(function_1("hello"))
print(output) # Hellohello



### Multiple return values

# Functions terminate at the return keyword. 
# If you write code below the return statement that code will not be executed.
# However, you can have multiple return statements in one function. So how does that work?

## Conditional Returns
# When we have control flow, as in the code will behave differently (go down different execution paths) depending on certain 
# conditional checks, we can end up with multiple endings (returns).
# e.g.

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False

## Empty Returns
# You can also write return without anything afterwards, and this just tells the function to exit.
# e.g.

def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit and return nothing.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
    
## Challenge: Check for leap years   
def is_leap_year(year):
    if year % 400 == 0:  # Alle durch 400 teilbaren Jahre sind Schaltjahre
        return True
    if year % 100 == 0:  # Alle durch 100 teilbaren Jahre sind KEINE Schaltjahre (au�er durch 400 teilbare)
        return False
    if year % 4 == 0:  # Alle durch 4 teilbaren Jahre sind Schaltjahre
        return True
    return False  # Alle anderen Jahre sind keine Schaltjahre
        
# Testfall
print(is_leap_year(2022))  # Erwartete Ausgabe: False
print(is_leap_year(2020))  # Erwartete Ausgabe: True
print(is_leap_year(2000))  # Erwartete Ausgabe: True
print(is_leap_year(1900))  # Erwartete Ausgabe: False

### Docstrings
# You can use docstrings to write multiline comments that document your code.

## Syntax
# Just enclose your text inside a pair of three double quotes.
# e.g.

""" 
My 
Multiline 
Comment 
"""

## Documenting Functions
# A neat feature of docstrings is you can use it just below the definition of a function and that text will be displayed when you hover over a function call. 
# It's a good way to remind yourself what a self-created function does.
# e.g.

def my_function(num):
    """Multiplies a number by itself."""
    return num * num