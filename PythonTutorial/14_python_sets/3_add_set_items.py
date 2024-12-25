
# Python - Add Set Items


# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
#
# To add one item to a set use the add() method.

# ex:
# Add an item to a set, using the add() method:
set1 = {"apple", "banana", "cherry"}
set1.add("orange")

print(set1)


# Add Sets
# To add items from another set into the current set, use the update() method.
# ex:
# Add elements from tropical into set2:
set2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

set2.update(tropical)
print(set2)


# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# ex:
# Add elements of a list to at set:
set3 = {"apple", "banana", "cherry"}
tropical = ["pineapple", "mango", "papaya"]
set3.update(tropical)
print(set3)
