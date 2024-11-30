
# Python - Access Tuple Items

# Access Tuple Items,
# You can access tuple items by referring to the index number, inside square brackets:
# ex:
# Print the second item in the tuple:
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1])
# Note: the first item has index 0

# Negative Indexing:
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

# ex:
# Print the last item of the tuple:
print(this_tuple[-1])


# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
#
# When specifying a range, the return value will be a new tuple with the specified items.

# ex:
# Return the third, fourth, and fifth item:
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.


# By leaving out the start value, the range will start at the first item:
# ex: This example returns the items from the beginning to, but NOT included, "kiwi":
print(this_tuple[:4])

# By leaving out the end value, the range will go on to the end of the tuple:
# ex: This example returns the items from "cherry" and to the end:
print(this_tuple[2:])


# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:
# ex: This example returns the items from index -4 (included) to index -1 (excluded)
print(this_tuple[-4:-1])


# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
# Check if "apple" is present in the tuple:
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
    print("Yes, 'apple' is in the fruits tuple")
