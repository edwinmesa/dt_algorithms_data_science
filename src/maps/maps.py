# Squaring a list of numbers using map()
numbers = [1, 2, 3, 4, 5]
def square(num):
    return num ** 2
square_nums = map(square, numbers)
print("Squares: ", list(square_nums))
print("Time Complexity: O(n^2)")
print('#' * 80)

# Converting a list of integers to their corresponding binary representation using map()
numbers = [10, 20, 30, 40, 50]
def int_to_binary(x):
    return bin(x)[2:] # remove '0b' from the beginning.
bin_represenations = map(int_to_binary, numbers)
print("List Binary", list(bin_represenations))
print("Time Complexity: O(n^2)")
print('#' * 80)

# Using map() with lambda function to perform multiple operations on a list

import numpy as np
from array import array
# Example: Converting map with multiple operations on a list to an array
numbers = [1, 2, 3, 4, 5]
# Using map to apply three operations on each number
result_map = map(lambda x: (x, x**2, x**3, x*2), numbers)
# Convert the map object to a list
# result_list = list(result_map)
# Create an array from the list
result_array = array('i', [item[0] + item[1] - item[2] + item[3] for item in result_map])
# result_array = np.array(result_array)
result_array = list(result_array)
print(result_array)  # Output: array('i', [1, 6, 27, 16, 35])

print("Time Complexity: O(n)")
print('#' * 80)

from array import array
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
# Define the operations using a lambda function
operations = lambda x, y: (x + y, x * y)
# Apply the operations using map
result_map = map(operations, numbers1, numbers2)
# Convert the map object to a list
# result_list = list(result_map)
# Create an array from the list
result_array = array('i', [item[0] - item[1] for item in result_map])
result_array = list(result_array)
print(result_array)
print("Time Complexity: O(n)")
print('#' * 80)

# Combine elements from both lists using a lambda function
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
result   = map(lambda x, y: x + y, numbers1, numbers2)
print("List Combined", list(result))
print("Time Complexity: O(n)")
print('#' * 80)

# Calculating factorial of a list of numbers using map() and reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

factorials = map(factorial, numbers)
print("list factorial: ", list(factorials))
print("Time Complexity: O(n)")
print('#' * 80)

# Using map() with multiple iterables of different lengths
names       = ['Alice', 'Bob', 'Charlie']
ages        = [25, 30, 27, 22, 35]
countries   = ['USA', 'Canada', 'UK']
# Zip the iterables and combine their elements using a lambda function
result      = map(lambda x :f"Name: {x[0]}, Age: {x[1]}, Country: {x[2]}", zip(names, ages, countries))
print("Combines with Map and Zip:", list(result))
print("Time Complexity: O(n)")
print('#' * 80)

#  Mapping multiple functions on a list of numbers
numbers = [1, 2, 3, 4, 5]

def add_one(x):
    return x + 1

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Apply multiple functions using a lambda function with map()
result = map(lambda x : (x, add_one(x), square(x), cube(x)), numbers)
print("map multiple functions", list(result))
print("Time Complexity: O(n)")
print('#' * 80)

# Using map() to convert a list of Celsius temperatures to Fahrenheit
celsius_temperatures = [0, 20, 35, 15]

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

farenheit_temp = map(celsius_to_fahrenheit, celsius_temperatures)
print('Farenheit Temperature:', list(farenheit_temp))
print("Time Complexity: O(n)")
print('#' * 80)

# Applying a series of transformations on a list of strings using map()
words = ['hello', 'world', 'python', 'programming']
# Combine various string transformations using a lambda function with map()
transformed_words = map(lambda x : x.upper()[::-1], words)
print("transformed words",list(transformed_words))
print("Time Complexity: O(n)")
print('#' * 80)

# Using map() with complex numbers to calculate the magnitude
complex_numbers = [2 + 3j, 1 - 2j, 4 + 4j]

def magnitude(c):
    return abs(c)**2 # Magnitude is calculated by taking absolute value first then squaring it

magnitudes = map(magnitude, complex_numbers)
print('Magnitudes:', list(magnitudes))
print("Time Complexity: O(n)")
print('#' * 80)


import pyphen

words = ['apple', 'banana', 'cherry']
# Initialize the hyphenation dictionary
dic   = pyphen.Pyphen(lang='en')

# Use the hyphenation dictionary to count syllables of each word
syllable_counts = map(lambda word: len(dic.inserted(word).split('-')), words)
print("syllable_counts:", list(syllable_counts))
print("Time Complexity: O(n)")
print('#' * 80)

# Mapping a list of strings to a custom object using a class method
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    @classmethod
    def from_string(cls, book_str):
        title, author, year = book_str.split(',')
        return cls(title.strip(), author.strip(), int(year.strip()))

book_strings = ['Python for Data Science, John Smith, 2020', 'Deep Learning, Alice Johnson, 2019']
# Use the class method 'from_string' with map() to create Book objects
books = map(Book.from_string, book_strings)
for book in books: 
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")

print("Time Complexity: O(n)")
print('#' * 80)

# Using map() to convert a list of binary strings to integers
binary_strings = ['101', '1100', '11111','100111111']
# Convert each binary string to an integer using the int() function with map()
integers = map(lambda x: int(x, 2), binary_strings)
print("binary to Integers:",list(integers))
print("Time Complexity: O(n)")
print('#' * 80)