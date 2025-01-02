# Python Scope


# A variable is only available from inside the region it is created. This is called scope.
#
# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.


# example
# A variable created inside a function is available inside that function:
def my_func():
    x = 300
    print(x)


my_func()


# Function Inside Function
# As explained in the example above, the variable x is not available outside the function,
# but it is available for any function inside the function:

# example
# The local variable can be accessed from a function within the function:
def my_func():
    x = 300

    def my_inner_func():
        print(x)

    my_inner_func()


my_func()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#
# Global variables are available from within any scope, global and local.

# example
# A variable created outside a function is global and can be used by anyone:
x = 300


def my_func():
    print(x)


my_func()
print(x)

# Naming Variables
# If you operate with the same variable name inside and outside a function,
# Python will treat them as two separate variables, one available in the global scope (outside the function)
# and one available in the local scope (inside the function):
#
# example
# The function will print the local x, and then the code will print the global x:
x = 300


def my_func():
    x = 100
    print(x)


my_func()
print(x)


# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#
# The global keyword makes the variable global.
#
# example
# If you use the global keyword, the variable belongs to the global scope:

def my_func():
    global g_x
    g_x = 200
    print(g_x)


my_func()
print(g_x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.

# example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300


def my_func():
    global x
    x = 150
    print(x)


my_func()
print(x)


# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.
#
# The nonlocal keyword makes the variable belong to the outer function.
#
# example
# If you use the nonlocal keyword, the variable will belong to the outer function:

def my_func1():
    x = "Jane"

    def my_func2():
        nonlocal x
        x = "hello"

    my_func2()
    return x


print(my_func1())
