
# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.


# Upper Case
# Example
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())


# Lower Case
# Example
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


# Remove Whitespace.
# Whitespace is the space before and/or after the actual text, and very ofen you want to remove this space.
# Example
# The strip() method removes any whitespace from the beginning or the end:
a = "  Hello, World!  "
print(a.strip())    # returns "Hello, World!"


# Replace String
# Example
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))


# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
# Example
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', 'World!']


# String Methods
# Learn more about String Methods with our String Methods Reference
# https://www.w3schools.com/python/python_ref_string.asp


# Exercise
# What is a correct syntax to print a string in upper case letters?
"Welcome".upper()


# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
print(x)


# Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()


# Convert the value of txt to lower case.
txt = "Hello World"
txt.lower()


# Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")
