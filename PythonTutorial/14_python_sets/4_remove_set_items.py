
# Python - Remove Set Items

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# ex: remove()
# Remove "banana" by using the remove() method:
set1 = {"apple", "banana", "cherry"}
set1.remove("banana")
print(set1)
# Note: If the item to remove does not exist, remove() will raise an error.


# ex: discard()
# Remove "banana" by using the discard() method:
set2 = {"apple", "banana", "cherry"}
set2.discard("banana")
print(set2)
# Note: If the item to remove does not exist, discard() will NOT raise an error.


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#
# The return value of the pop() method is the removed item.
# ex:
# Remove a random item by using the pop() method:
set3 = {"apple", "banana", "cherry"}
pop_return_value = set3.pop()
print(pop_return_value)
print(set3)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


# clear()
# The clear() method empties the set:
set4 = {"apple", "banana", "cherry"}
set4.clear()
print(set4)


# del()
# The del keyword will delete the set completely:
set5 = {"apple", "banana", "cherry"}
del set5
# print(set5)
