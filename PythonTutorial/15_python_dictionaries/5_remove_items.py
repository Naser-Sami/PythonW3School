

# Python - Remove Dictionary Items

# Removing Items
# There are several methods to remove items from a dictionary:


# pop()
# The pop() method removes the item with the specified key name:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop('model')
print(car)


# popitem()
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car)


# del()
# The del keyword removes the item with the specified key name:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del car['brand']
print(car)


# The del keyword can also delete the dictionary completely:
del car
# print(car)


# clear()
# The clear() method empties the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print(car)
