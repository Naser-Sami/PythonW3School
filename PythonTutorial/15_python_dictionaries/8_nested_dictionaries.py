# Python - Nested Dictionaries


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Create a dictionary that contain three dictionaries:
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Or, if you want to add three dictionaries into a new dictionary:
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

my_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Print the name of child 2:
print(my_family['child2']['name'])

# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this:
#
# Loop through the keys and values of all nested dictionaries:
for x, obj in my_family.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
