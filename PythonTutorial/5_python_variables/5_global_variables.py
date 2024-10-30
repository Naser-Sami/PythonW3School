# Python - Global Variables

# Global variables.
# Variables that are created outside a function ( as in all the examples in the previous pages )
# are known as global variables.

# Global variables, can be used by everyone, both inside of function and outside.

# Example:
x = "awesome"


def my_func():
    print("Python is " + x)


my_func()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used
# inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)


# ------------------------

# The global Keyword Normally, when you create a variable inside a function, that variable is local, and can only be
# used inside the function.

# To create a global variable inside a function, you can use the global keyword.
# Example:
# If you use the global keyword, the variable belongs to the global scope:
def my_func():
    global x
    x = "fantastic"


my_func()
print("Python is " + x)


# Also, use the global keyword if you want to change a global variable inside a function.
global_name = "Awesome"


def any_func():
    global global_name
    global_name = "Fantastic"


any_func()
print("Python is " + global_name)
