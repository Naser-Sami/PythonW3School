
# Python - Loop Tuples

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

# Ex:
# Iterate through the items and print the values:
this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.
#
# Use the range() and len() functions to create a suitable iterable.

# Ex:
print("For loop")
# Print all items by referring to their index number:
this_tuple = ("apple", "banana", "cherry")
for i in range(len(this_tuple)):
    print(i, end=': ')
    print(this_tuple[i])


# Using a While Loop
print("While loop")
# You can loop through the tuple items by using a while loop.
#
# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
#
# Remember to increase the index by 1 after each iteration.
count = 0
while count < len(this_tuple):
    print(count, end=': ')
    print(this_tuple[count])
    count += 1
