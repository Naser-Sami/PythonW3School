
# Python - Access List Items

# Access Items
# List items are indexed, and you can access them by referring to the index number:
# ex:
# Print the second item of the list:
this_list = ["apple", "banana", "cherry"]
print(this_list[1])
# Note: The first item has index 0


# Negative Indexing,
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# ex:
# Print the last item of the list:
this_list = ["apple", "banana", "cherry"]
print(this_list[-1])


# Range of Indexes,
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.


# By leaving out the start value, the range will start at the first item:
# ex:
# This example returns the items from the beginning to, but NOT including, "kiwi":
print(this_list[:4])

# By leaving out the end value, the range will go on to the end of the list:
# ex:
# This example returns the items from "cherry" to the end:
print(this_list[2:])


# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# ex:
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
print(this_list[-4:-1])


# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# ex:
# Check if "apple" is present in the list:
if "apple" in this_list:
    print("Yes, 'apple' is in the fruits list")


