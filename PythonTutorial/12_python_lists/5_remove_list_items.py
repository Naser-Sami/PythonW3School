
# Python - Remove List Items


# Remove Specified Item:
# The remove() method removes the specified item.
# ex:
# remove 'banana'
this_list = ["apple", "banana", "cherry"]
this_list.remove('banana')
print(this_list)


# If there are more than one item with the specified value,
# the remove() method removes the first occurrence:
# ex:
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]
this_list.remove('banana')
print(this_list)


# Remove Specified Index
# The pop() method removes the specified index.
# ex:
# Remove the second item
this_list = ["apple", "banana", "cherry"]
this_list.pop(1)
print(this_list)

# if you do not specify the index, the pop() method removes the last item.
# ex:
# Remove the last item:
this_list = ["apple", "banana", "cherry"]
this_list.pop()
print(this_list)


# The del keyword also removes the specified index:
# ex:
# Remove the first item:
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]
del this_list[0]
print(this_list)

# The del keyword can also delete the list completely:
# ex:
# Delete the entire list:
del this_list
# print(this_list) # NameError: name 'this_list' is not defined


# Clear the list
# The clear() method empties the list
# The list still remains, but it has no content.
# ex:
# Clear the list content:
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)
