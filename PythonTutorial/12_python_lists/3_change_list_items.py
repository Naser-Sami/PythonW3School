
# Python - Change List Items

# Change Item Value
# To change the value of a specific item, refer to the index number:

# ex:
# Change the second item:
this_list = ["apple", "banana", "cherry"]
this_list[1] = 'blackcurrant'
print(this_list)


# Change a Range of Item Values
# To change the value of items within a specific range,
# define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values:

# ex:
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)


# If you insert more items than you replace,
# the new items will be inserted where you specified,
# and the remaining items will move accordingly:

# ex:
# Change the second value by replacing it with two new values:
this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)
# Note: The length of the list will change when the number of items inserted
# does not match the number of items replaced.


# If you insert less items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly:

# ex:
# Change the second and third value by replacing it with one value:
this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)


# Insert Items
# To insert a new list item, without replacing any of the existing values,
# we can use the insert() method.

# The insert() method inserts an item at the specified index:
# ex:
# Insert "watermelon" as the third item:

this_list = ["apple", "banana", "cherry"]
this_list.insert(2, "watermelon")
print(this_list)
# Note: As a result of the example above, the list will now contain 4 items.
