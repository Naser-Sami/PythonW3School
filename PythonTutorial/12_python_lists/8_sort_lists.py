
# Python - Sort List,

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Sort the list alphabetically:

alphabetically_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
alphabetically_list.sort()
print(alphabetically_list)

# Sort the list numerically:
numeric_list = [100, 50, 65, 82, 23]
numeric_list.sort()
print(numeric_list)


# Sort Descending

# To sort descending, use the keyword argument reverse = True:
# Sort the list descending:
alphabetically_list.sort(reverse=True)
print(alphabetically_list)

numeric_list.sort(reverse=True)
print(numeric_list)


# Customize Sort Function

# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

# Sort the list based on how close the number is to 50:
def my_func(n):
    return abs(n - 50)


list = [100, 50, 65, 82, 23]
list.sort(key=my_func)
print(list)


# Case Insensitive Sort

# By default the sort() method is case sensitive,
# resulting in all capital letters being sorted before lower case letters:

# Case-sensitive sorting can give an unexpected result:
new_list = ["banana", "Orange", "kiwi", "cherry"]
new_list.sort()
print(new_list)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

# Perform a case-insensitive sort of the list:
new_list.sort(key=str.lower)
print(new_list)


# Reverse Order

# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.

# Reverse the order of the list items:
new_list = ["banana", "Orange", "kiwi", "cherry"]
new_list.reverse()
print(new_list)
