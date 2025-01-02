
# Python Modules

# What is a Module?
# Consider a module to be the same as a code library.
#
# A file containing a set of functions you want to include in your application.
#
# Create a Module
# To create a module just save the code you want in a file with the file extension .py:

# Save this code in a file named mymodule.py


# Use a Module
# Now we can use the module we just created, by using the import statement:
# Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")
# Note: When using a function from a module, use the syntax: module_name.function_name.

#  access the person1 dictionary:
a = mymodule.person1["age"]
print(a)

print('-' * 20)
print('Show all methods in mymodule:')
print(dir(mymodule))
print('-' * 20)

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# Example
# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)


# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
#
# Example
# Import and use the platform module:

import platform

x = platform.system()
print(x)


# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
#
# Example
# List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)
# Note: The dir() function can be used on all modules, also the ones you create yourself.


# Import From Module
# You can choose to import only parts from a module, by using the 'from' keyword.
#
# Example
# The module named mymodule has one function and one dictionary:

# Import only the person1 dictionary from the module:

from mymodule import person1

print(person1["age"])
