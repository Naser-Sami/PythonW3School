
# Python - Loop Dictionaries

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
#
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one:
for key in car:
    print(key)

# Print all values in the dictionary, one by one:
for key in car:
    print(car[key])

# You can also use the values() method to return values of a dictionary:
for value in car.values():
    print(value)

# You can use the keys() method to return the keys of a dictionary:
for key in car.keys():
    print(key)

# Loop through both keys and values, by using the items() method:
for key, value in car.items():
    print(key, value)


