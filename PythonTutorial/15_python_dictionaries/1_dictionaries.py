# Python Dictionaries

# Dictionary
# Dictionaries are used to store data values in key:value pairs.
#
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#
# Dictionaries are written with curly brackets, and have keys and values:


# Create and print a dictionary:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)

# Dictionary Items,
# Dictionary items are ordered, changeable, and do not allow duplicates.
#
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# Print the "brand" value of the dictionary:
print(this_dict["brand"])

# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
#
# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#
# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values:
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(this_dict)

# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
#
# Print the number of items in the dictionary:
print(len(this_dict))

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
#
# Example
# String, int, boolean, and list data types:

this_dict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
#
# <class 'dict'>
print(type(this_dict))

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
#
# Example
# Using the dict() method to make a dictionary:
this_dict = dict(name="John", age=36, country="Norway")
print(this_dict)
