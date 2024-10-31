
# Python - String Methods

# String Methods
# Python has a set of built-in methods that you can use on strings.


# Note: All string methods return new values. They do not change the original string.

# Method	        Description
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()          Returns an encoded version of the string
# endswith()        Returns true if the string ends with the specified value
# expandtabs()      Sets the tab size of the string
# find()            Searches the string for a specified value and returns the position of where it was found
# format()          Formats specified values in a string
# format_map()      Formats specified values in a string
# index()           Searches the string for a specified value and returns the position of where it was found
# isalnum()         Returns True if all characters in the string are alphanumeric
# isalpha()         Returns True if all characters in the string are in the alphabet
# isascii()         Returns True if all characters in the string are ascii characters
# isdecimal()       Returns True if all characters in the string are ascii characters
# isdigit()         Returns True if all characters in the string are digits
# isidentifier()    Returns True if the string is an identifier
# islower()         Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Converts the elements of an iterable into a string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning


# region - Python String capitalize() Method

print("Python String capitalize() Method")

# Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

# Definition and Usage
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

# Syntax
# string.capitalize()
# Parameter Values
# No parameters

# More Examples.
# Example
# The first character is converted to upper case, and the rest are converted to lower case:
txt = "python is FUN!"
x = txt.capitalize()
print(x)

# Example
# See what happens if the first character is a number:
txt = "36 is my age."
x = txt.capitalize()
print(x)

print()

# endregion

# region - Python String casefold() Method

print("Python String casefold() Method")

# Example
# Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# Definition and Usage
# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger,
# more aggressive, meaning that it will convert more characters into lower case,
# and will find more matches when comparing two strings and both are converted using the casefold() method.

# Syntax
# string.casefold()

# Parameter Values
# No parameters

print()

# endregion

# region - Python String center() Method

print("Python String center() Method")

# Example
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"
x = txt.center(20)
print(x)

# Definition and Usage
# The center() method will center align the string,
# using a specified character (space is default) as the fill character.

# Syntax
# string.center(length, character)

# Parameter     Values
# Parameter	    Description
# length	    Required. The length of the returned string
# character	    Optional. The character to fill the missing space on each side. Default is " " (space)

# More Examples
# Using the letter "O" as the padding character:

txt = "banana"
x = txt.center(20, "O")
print(x)

# endregion

# region - Python String count() Method

print("Python String count() Method")

# Example
# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


# Definition and Usage
# The count() method returns the number of times a specified value appears in the string.

# Syntax
# string.count(value, start, end)

# Parameter     Values
# Parameter	    Description
# value	        Required. A String. The string to value to search for
# start	        Optional. An Integer. The position to start the search. Default is 0
# end	        Optional. An Integer. The position to end the search. Default is the end of the string

# More Examples
# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# endregion

# region - Python String encode() Method
print("Python String encode() Method")

# Example
# UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)

# Definition and Usage
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

# Syntax
# string.encode(encoding=encoding, errors=errors)


# Parameter         Values
# Parameter	        Description
# encoding	        Optional. A String specifying the encoding to use. Default is UTF-8
# errors	        Optional. A String specifying the error method. Legal values are:
#                       'backslashreplace'	- uses a backslash instead of the character that could not be encoded
#                       'ignore'	- ignores the characters that cannot be encoded
#                       'namereplace'	- replaces the character with a text explaining the character
#                       'strict'	- Default, raises an error on failure
#                       'replace'	- replaces the character with a questionmark
#                       'xmlcharrefreplace'	- replaces the character with an xml character

# More Examples
# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endregion

# region - Python String endswith() Method
print("Python String endswith() Method")

# Example
# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# Definition and Usage
# The endswith() method returns True if the string ends with the specified value, otherwise False.

# Syntax
# string.endswith(value, start, end)

# Parameter         Values
# Parameter	        Description
# value	            Required. The value to check if the string ends with
# start	            Optional. An Integer specifying at which position to start the search
# end	            Optional. An Integer specifying at which position to end the search


# More Examples
# Check if the string ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)


# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# endregion

# region
# endregion

# region
# endregion

# region
# endregion

# region
# endregion

# region
# endregion

# region
# endregion
