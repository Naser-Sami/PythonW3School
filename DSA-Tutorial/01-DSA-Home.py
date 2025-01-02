
# DSA Tutorial

# Learn Data Structures and Algorithms
# Data Structures and Algorithms (DSA) is a fundamental part of Computer Science that teaches you how to think and solve complex problems systematically.
#
# Using the right data structure and algorithm makes your program run faster, especially when working with lots of data.
#
# Knowing DSA can help you perform better in job interviews and land great jobs in tech companies.

# https://www.w3schools.com/dsa/index.php


# This Tutorial,
# This tutorial is made to help you learn Data Structures and Algorithms (DSA) fast and easy.
#
# Animations, like the one below, are used to explain ideas along the way.


# First, you will learn the fundamentals of DSA: understanding different data structures, basic algorithm concepts,
# and how they are used in programming.
#
# Then, you will learn more about complex data structures like trees and graphs,
# study advanced sorting and searching algorithms, explore concepts like time complexity, and more.
#
# This tutorial will give you a solid foundation in Data Structures and Algorithms, an essential skill for any software developer.


# Try it Yourself Examples in Every Chapter
# In every chapter, you can edit the examples online, and click on a button to view the result.
#
# The code examples in this tutorial are written in Python, C, and Java. You can see this by clicking the "Run Example" button.

# Example
my_array = [7, 12, 9, 4, 11]


def find_min_value(array):
    min_val = array[0]
    for i in array:
        if i < min_val:
            min_val = i

    return min_val


def find_max_value(array):
    max_val = array[0]
    for i in array:
        if i > max_val:
            max_val = i

    return max_val


min_value = find_min_value(my_array)
print('Lowest value:', min_value)

max_value = find_max_value(my_array)
print('Max value:', max_value)


# DSA History
# The word 'algorithm' comes from 'al-Khwarizmi', named after a Persian scholar who lived around year 800.
#
# The concept of algorithmic problem-solving can be traced back to ancient times, long before the invention of computers.
#
# The study of Data Structures and Algorithms really took off with the invention of computers in the 1940s, to efficiently manage and process data.
#
# Today, DSA is a key part of Computer Science education and professional programming, helping us to create faster and more powerful software.
