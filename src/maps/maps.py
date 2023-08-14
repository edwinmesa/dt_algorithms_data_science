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
