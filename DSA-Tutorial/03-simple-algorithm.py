# A Simple Algorithm


# Fibonacci Numbers

# The two first Fibonacci numbers are 0 and 1,
# and the next Fibonacci number is always the sum of the two previous numbers,
# so we get 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# How it works:
#
# 1. Start with the two first Fibonacci numbers 0 and 1.
#   a. Add the two previous numbers together to create a new Fibonacci number.
#   b. Update the value of the two previous numbers.
# 2. Do point a and b above 18 times.


print(0)
print(1)
count = 0


def fibonacci_numbers(prev1, prev2):
    global count
    if count <= 10:
        new_fibo = prev1 + prev2
        print(new_fibo)
        prev2 = prev1
        prev1 = new_fibo
        count += 1
        fibonacci_numbers(prev1, prev2)
    else:
        return


fibonacci_numbers(1, 0)

# Basic Structure of Recursive Function
#
# def recursive_function(parameters):
#     if base_case_condition:
#         return base_result
#     else:
#         return recursive_function(modified_parameters)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         x= n * factorial(n - 1)
#         # print(x)
#         return x
#
#
# print(factorial(5))
