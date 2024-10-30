
# Python Data Types

# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

#   Text type:          str
#   Numeric type:       int, float, complex
#   Sequence type:      list, tuple, range
#   Mapping type:       dict
#   Set type:           set, frozenset
#   Boolean type:       bool
#   Binary types:       bytes, bytearray, memoryview
#   None type:          NoneType


# Getting the Data Type
# You can get the data type of any object by using the type() function:

# Print the data type of the variable x:
x = 5
print(type(x))


# Setting the Data Type
# In python, the data types is set when you assign a value to a variable:

# Example                                                   # Data Type
x = "Hello, World"                                          # str
x = 20                                                      # int
x = 20.5                                                    # float
x = 1j                                                      # complex
x = ["apple", "banana", "cherry"]                           # list
x = ("apple", "banana", "cherry")                           # tuple
x = range(6)                                                # range
x = {"name": "John", "age": 36}                             # dict
x = {"apple", "banana", "cherry"}                           # set
x = frozenset({"apple", "banana", "cherry"})                # frozenset
x = True                                                    # bool
x = b"Hello"                                                # bytes
x = bytearray(5)                                            # bytearray
x = memoryview(bytes(5))                                    # memoryview
x = None                                                    # NoneType


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example                                                   # Data Type
x = str("Hello, World")                                     # str
x = int(20)                                                 # int
x = float(20.5)                                             # float
x = complex(1j)                                             # complex
x = ["apple", "banana", "cherry"]                           # list
x = ("apple", "banana", "cherry")                           # tuple
x = range(6)                                                # range
x = {"name": "John", "age": 36}                             # dict
x = {"apple", "banana", "cherry"}                           # set
x = frozenset({"apple", "banana", "cherry"})                # frozenset
x = True                                                    # bool
x = b"Hello"                                                # bytes
x = bytearray(5)                                            # bytearray
x = memoryview(bytes(5))                                    # memoryview
