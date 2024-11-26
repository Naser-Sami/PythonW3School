# Python - List Comprehension

# List Comprehension,
# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.

# ex:
# Based on a list of fruits,
# you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)

# With list comprehension you can do all that with only one line of code:
# ex:
new_list = [x for x in fruits if "a" in x]
print(new_list)

# The Syntax
# list = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.


# Condition
# The condition is like a filter that only accepts the items that valuate to True.
# ex:
# Only accept items that are not "apple":
new_list = [x for x in fruits if "apple" not in x]
# new_list = [x for x in fruits if x != "apple"]
print(new_list)

# The condition if x != "apple"  will return True for all elements other than "apple",
# making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:
# With no if statement:
new_list = [x for x in fruits]
print(new_list)


# The expression can also contain conditions,
# not like a filter, but as a way to manipulate the outcome:
# ed:
# Return "orange" instead of "banana":
new_list = [x if x != 'banana' else 'orange' for x in fruits]
print(new_list)

