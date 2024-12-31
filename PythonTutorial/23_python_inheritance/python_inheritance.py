
# Python Inheritance


# Python Inheritance,
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.
#
# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:


# ex:
# Create a class named Person, with firstname and lastname properties, and a print_name method:

class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def print_name(self):
        print(self.f_name, self.l_name)


# Use the Person class to create an object, and then execute the print_name method:
p1 = Person("Naser", "Sami")
p1.print_name()


# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass


s1 = Student("Naser", "Ebedo")
s1.print_name()


# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
#
# We want to add the __init__() function to the child class (instead of the pass keyword).
#
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Add the __init__() function to the Student class:
class Student(Person):

    # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    #
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, f_name, l_name):
        # add properties etc.
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        Person.__init__(self, f_name, l_name)


x = Student("X", "Y")
x.print_name()


# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)

        # Add Properties
        # Add a property called graduation_year to the Student class:
        self.graduation_year = 2019

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


s1 = Student("Naser", "Ebedo")
s1.print_name()
print(s1.graduation_year)


# In the example below, the year 2019 should be a variable,
# and passed into the Student class when creating student objects. To do so,
# add another parameter in the __init__() function:

# Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
    def __init__(self,f_name, l_name, year):
        super().__init__(f_name, l_name)

        self.graduation_year = year


s1 = Student("Naser", "Sami", 2016)

s1.print_name()
print(s1.graduation_year)


# Add Methods
# Example
# Add a method called welcome to the Student class:

class Student(Person):
    def __init__(self,f_name, l_name, year):
        super().__init__(f_name, l_name)

        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.f_name, self.l_name, "to the class of", self.graduation_year)
# If you add a method in the child class with the same name as a function in the parent class,
# the inheritance of the parent method will be overridden.


s2 = Student("Naser", "Sami", 2016)
s2.welcome()

