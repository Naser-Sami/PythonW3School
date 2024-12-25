
# Python - Join Sets

# Join Sets
# There are several ways to join two or more sets in Python.
#
# The union() and update() methods joins all items from both sets.
#
# The intersection() method keeps ONLY the duplicates.
#
# The difference() method keeps the items from the first set that are not in the other set(s).
#
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

print('\nUnion:\n')
# Union
# The union() method returns a new set with all items from both sets.
# Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

print('\nJoin Multiple Sets:\n')
# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.
#
# When using a method, just add more sets in the parentheses, separated by commas:

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set5 = set1.union(set2, set3, set4)
print(set5)

# When using the | operator, separate the sets with more | operators:
# Use | to join two sets:
set5 = set1 | set2 | set3 | set4
print(set5)

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
#
# The result will be a set.
# Join a set with a tuple:
my_set = {"a", "b", "c"}
my_tuple = (1, 2, 3)

join_set_tuple = my_set.union(my_tuple)
print(join_set_tuple)
# Note: The  | operator only allows you to join sets with sets,
# and not with other data types like you can with the  union() method.


print('\nUpdate:\n')
# Update
# The update() method inserts all items from one set into another.
#
# The update() changes the original set, and does not return a new set.
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.


print('\nIntersection:\n')
# Intersection
# Keep ONLY the duplicates
#
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set1)
print(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.
# Use & to join two sets:
set3 = set1 & set2
print(set3)
# Note: The & operator only allows you to join sets with sets,
# and not with other data types like you can with the intersection() method.


print('\nIntersection Update:\n')
# The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.
# Keep the items that exist in both set1, and set2:
set1.intersection_update(set2)
print(set1)
print(set2)

# The values True and 1 are considered the same value. The same goes for False and 0.
# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

