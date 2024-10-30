# Python - Escape Characters

# Escape Character

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:


# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

# To fix this problem, use the escape character \":
# Example
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# Escape Characters
# Other escape characters used in Python:

# Code	        Result
# \'	        Single Quote
# \"	        Double Quote
# \\            Backslash
# \n            New Line
# \r            Carriage Return
# \t            Tab
# \b            Backspace
# \f            Form Feed
# \ooo          Octal value
# \xhh          Hex value


txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

txt = "Hello \fWorld!"
print(txt)

# A backslash followed by three integers will result in octal value:
txt = "\110\145\154\154\157"
print(txt)

# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
