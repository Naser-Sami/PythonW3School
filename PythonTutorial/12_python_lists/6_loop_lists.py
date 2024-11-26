# Python - Loop Lists


# Loop Through a List
# You can loop through the list items by using a for loop:
# ex:
# Print all items in the list, one by one:
list = ["apple", "banana", "cherry"]
for x in list:
    print(x)

# Learn more about for loops in our Python For Loops Chapter.
# https://www.w3schools.com/python/python_for_loops.asp

print('-' * 40)

# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

# ex:
# Print all items by referring to their index number:
for i in range(len(list)):
    print(list[i])
# The iterable created in the example above is [0, 1, 2].


print('-' * 40)


# Using a While Loop,
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list,
# then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.

# ex:
# Print all items, using a while loop to go through all the index numbers

i = 0
while i < len(list):
    print(list[i])
    i += 1

# Learn more about while loops in our Python While Loops Chapter.
# https://www.w3schools.com/python/python_while_loops.asp


print('-' * 40)


# Looping Using List Comprehension,
# List Comprehension offers the shortest syntax for looping through lists:

# ex:
# A shorthand for loop that will print all items in a list:
[print(x) for x in list]

# Learn more about list comprehension in the next chapter: List Comprehension.
# https://www.w3schools.com/python/python_lists_comprehension.asp
