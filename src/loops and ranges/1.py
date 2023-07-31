# Nested Loop using range
# This example demonstrates a nested loop structure using the range function. 
# It prints out a multiplication table for numbers from 1 to 10.

# this example simulated a multiply table.
for i in range(2, 11):
    for j in range(2,11):
        result = i * j
        print(f"Result {i} x {j} = {result}")

print('#' * 80)

# Loop with Step Size using range
for num in range(0, 21, 2):
    print(num, end=" ")
print()    
print('#' * 80)

# Reverse Loop using range
for num in range(10, 0, -1):
    print(num, end=" ")
print()
print('#' * 80)

# Sum of Even Numbers in a Range using range
def sum_even_numbers(limit):
    total = 0
    for num in range(2, limit + 1, 2):
        total += num
    return total

limit        = 10
sum_of_evens = sum_even_numbers(limit) # calculate
print(f"The sum of even numbers from 1 to {limit} is: {sum_of_evens}")
print('#' * 80)

# Using range to iterate through a list and index
fruits = ["apple", "banana", "orange", "grape"]

for index in range(len(fruits)):
    print(f"Index: {index}, Fruit: {fruits[index]}")
print('#' * 80)

# Countdown Timer using range
import time

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time Remaining: {i} seconds")
        time.sleep(1)
    print("Time's up!")

sec = 3 
countdown_timer(sec)
print('#' * 80)

# Diamond Pattern using range

def print_diamonf_patter(size):
    for i in range(1, size + 1, 2):
        print(" " * ((size - i)//2) + "*" * i)
    for i in range(size - 2, 0, -2):
        print(" " * ((size - i)//2) + "*" * i)

diamond_example = 7
print_diamonf_patter(diamond_example)
print('#' * 80)

# Matrix Multiplication using range
matrix1       = [[1, 2], [3, 4]]
matrix2       = [[5, 6], [7, 8]]
result_matrix = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(result_matrix[i][j], "+=", matrix1[i][k], "->", matrix2[k][j])
            result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

print("Matrix Multiplication Result:")
for row in result_matrix:
    print(row)
