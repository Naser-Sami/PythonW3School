
# Python - Copy Dictionaries

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because:
#   dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().


# Make a copy of a dictionary with the copy() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car_copy = car.copy()
print(car_copy)


# Another way to make a copy is to use the built-in function dict().
my_dict = dict(car)
print(my_dict)
