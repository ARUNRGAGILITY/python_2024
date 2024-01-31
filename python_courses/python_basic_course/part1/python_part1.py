# Python Module1: Here we are going to practice the following

'''
1. Python Output statement
2. Python Basic data-types
3. Python Input statement
4. Python Comments
5. Python Type detection and casting
'''

###########################################################
# Python Output Statement
print('Hello World!')
print("Hello World!")
print("""Hello World!""")
my_name = "John S"
my_message = """
I am an Engineer
Working in MNC
I know Software Development
"""

print(f"Printing some details: {my_name}, {my_message}")
width = 10
height = 20
print("Area of a rectangle: ", width * height)
formatted_string = "FormatString: This is a rectangle details Width: {var1}, Height: {var2}".format(var1=width, var2=height)
print(formatted_string)

###########################################################
# Python Basic Data type
# int, float, string, boolean, complex number
width = 10
bank_balance = 100000.232
my_name = "John S"
is_employee = True
complex_num_example = 4 + 10j

print(f"Integer: {width}, Float: {bank_balance}, String: {my_name}, Boolean: {is_employee}, Complex Number: {complex_num_example}")

###########################################################
# Python Input Statement
get_name = str(input("Enter Your Name: "))
print(f"Hello {get_name}")
get_age = int(input("Enter Your Age: "))
print(f"Hello {get_name}, Your Age: {get_age}", get_age * 10)
get_bank_balance = float(input("Enter Your Bank Balance: "))
print(f"Hello {get_name}, Your Age: {get_age}, Your Bank Balnce: {get_bank_balance}", get_bank_balance * 20)


###########################################################
# Python Comments

# Single line comment

'''
This is
a
Multi-line comment
'''

"""
this is also 
a 
multi-line comment with double quotes
"""

def greet(message):
    """
    Documentation:
    this is greet function printing the message
    """
    print(message)
    
    
# calling the function
greet("Hello there!")
result = greet.__doc__
print(result)

# Class method documentation
class Myclass:
    """This is a docstring for Myclass."""

    def my_method(self):
        """This is a docstring for my_method of Myclass."""
        pass

print(Myclass.__doc__)
print(Myclass.my_method.__doc__)


###########################################################
# Type detection and type casting
width = 10
height = 10.5

# printing the type
print("Printing the type of the variable")
print(type(width))
print(type(height))