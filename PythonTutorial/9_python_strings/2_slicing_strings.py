
# Python - Slicing Strings

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and end index, separated by a colon, to return a part of the string.

# Example:
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
# Note: The first character has index 0.


# Slice from the start
# By leaving out the start index, the range will start at the first character:
# Example:
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])


# Slice To the End
# By leaving out the end index, the range will go to the end:
# Example:
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example:
# Get the characters:
#  - From: "o" in "World!" (position -5)
#  - To, but not included: "d" in "World!" (position -2)
b = "Hello, World!"
print(b[-5:-2])


# Exercise
# What will be the result of the following code:
x = 'Welcome'
print(x[3:5])


# Exercise: Python Slicing Strings
# Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
print(x)

# Exercise: Python Slicing Strings
# What will be the result of the following code:
x = 'Welcome'
print(x[3:])
