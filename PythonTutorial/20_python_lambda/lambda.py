
# Python Lambda
# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# The expression is executed and the result is returned:

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Lambda functions can take any number of arguments:
# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(1, 2, 3))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
#
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def my_func(n):
    return lambda a : a * n


# Use that function definition to make a function that always doubles the number you send in:
my_doubler = my_func(2)
print(my_doubler(11))

# Or, use the same function definition to make a function that always triples the number you send in:

my_tripler = my_func(3)
print(my_tripler(11))

# Or, use the same function definition to make both functions, in the same program:


def my_func(n):
    return lambda a : a * n


my_doubler = my_func(2)
my_tripler = my_func(3)

print(my_doubler(11))
print(my_tripler(11))
