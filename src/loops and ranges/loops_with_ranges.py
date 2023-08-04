# Sum of Array Elements using a Loop

# Example 1
def sum_array_elements(array):
    total_sum = 0
    for num in array:
        total_sum += num
    return total_sum

# Example usage
array  = [1, 2, 3, 4, 5]
result = sum_array_elements(array)
print(f"The sum of elements in the array is: {result}")
print("Time Complexity: O(n)")
print('#' * 80)

# Example 2
# Finding Maximum and Minimum Elements in an Array using a Loop
def find_max_min_elements(arr):
    max_element = arr[0]
    min_element = arr[0]
    # Traverse through all element to get maximum value and minimum value
    for num in arr:
        if (num > max_element):
            max_element = num
        if (num < min_element):
            min_element = num
    return max_element, min_element
# Example usage
array = [8, 3, 10, 1, 6]
max_value, min_value = find_max_min_elements(array)
print(f"Maximum element: {max_value}")
print(f"Minimum element: {min_value}")
print("Time Complexity: O(n)")
print('#' * 80)

# Example 3
# Reversing an Array using a Loop
def reverse_array(arr):
    reversed_array = []
    for i in range(len(arr) -1, -1,-1):
        reversed_array.append(arr[i])
    return reversed_array
# Example usage
array          = [1, 2, 3, 4, 5, 6, 9]
reversed_array = reverse_array(array)
print(f"Reversed Array :{reversed_array}")
print(f"Original Array :{array}")
print("Time Complexity: O(n)")
print('#' * 80)

# Counting Even and Odd Numbers in an Array using a Loop
def count_even_odd_numbers(arr):
    even_count = 0
    odd_count  = 0
    for num in arr:
        # If number is divisible by two then it's an even number else its an odd one
        if num % 2 == 0:
            even_count += 1
        # Else add one
        else:
            odd_count += 1
    return even_count, odd_count
# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
even, odd = count_even_odd_numbers(array)
print(f"{even}: numbers are even")
print(f"{odd}: numbers are odd")
print("Time Complexity: O(n)")
print('#' * 80)

# Array Filtering using a Loop
# This example filters an array to keep only elements greater than a given threshold.

def filter_array(arr, threshold):
    filtered_arr = []
    for elem in arr:
        if elem > threshold:
            filtered_arr.append(elem)
    return filtered_arr

# Example usage
array           = [10, 20, 5, 30, 15, 25]
threshold_value = 15
filtered_array  = filter_array(array, threshold_value)
print(f"Original array: {array}")
print(f"Filtered array (elements greater than {threshold_value}): {filtered_array}")
print("Time Complexity: O(n)")
print('#' * 80)

# Removing Duplicates from an Array using a Loop
# This example removes duplicate elements from an array using a loop.
def remove_duplicates(arr):
    unique_arr = []
    for num in arr:
        if not any([num == x for x in unique_arr]):   # check whether the
        #   if num not in unique_arr: 
            unique_arr.append(num)                  # element already exists or not
    return unique_arr

# Example usage
array        = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_array = remove_duplicates(array)
print(f"Array with duplicates removed: {unique_array}")
print(f"Original array: {array}")
print("Time Complexity: O(n)")
print('#' * 80)

# Array Sorting using a Loop
# This example sorts an array in ascending order using a loop.
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = selection_sort(array)
print(f"Sorted array: {sorted_array}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Array Concatenation using a Loop
# This example concatenates two arrays using a loop.

def concatenate_arrays(arr1, arr2):
    concatenated_arr = arr1.copy()
    for num in arr2:
        concatenated_arr.append(num)
    return concatenated_arr

# Example usage
array1 = [1, 2, 3]
array2 = [4, 5, 6]
concatenated_array = concatenate_arrays(array1, array2)
print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Concatenated array: {concatenated_array}")
print("Time Complexity: O(n)")
print('#' * 80)

# Array Repeating using a Loop
# This example repeats each element of an array a given number of times using a loop.

def repeat_elements(arr, times):
    repeat_arr = []
    for num in arr:
        repeat_arr.extend([num] * times)
        # Alternative implementation without the use of extend method (not recommended as it creates new list object)
    return repeat_arr

# Example usage
array           = [1, 2, 3]
repeat_times    = 3
repeated_array  = repeat_elements(array, repeat_times)
print(f"Original array: {array}")
print(f"Array with elements repeated {repeat_times} times: {repeated_array}")
print("Time Complexity: O(n)")
print('#' * 80)

# Two-Dimensional Array Sum using Nested Loops
# This example calculates the sum of elements in a two-dimensional array using nested loops.

# Example usage
def sum_2d_array(arr):
    total_sum = 0
    for row in arr:
        for num in row:
            total_sum += num
    return total_sum

# Example usage
two_d_array  = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_2d_arrays = sum_2d_array(two_d_array)
print("Sum 2d dimesional arrays", sum_2d_arrays)

# this code could be calculate with list comprehension
# Go....
# sum_arr = sum([sum(x) for x in two_d_array])
# print("Using Comprehension List: ",sum_arr)
print("Time Complexity: O(n)")
print('#' * 80)

# Fibonacci Sequence using range
# This example generates the Fibonacci sequence up to a specified number of terms.

def fibonacci_sequence(num_terms):
    fibonacci_list = [0, 1]
    for i in range(2, num_terms):
        # print(fibonacci_list[-1],  fibonacci_list[-2])
        next_term = fibonacci_list[-1] + fibonacci_list[-2]
        # append new term at end of list and remove first item from beginning (FIFO)
        fibonacci_list.append(next_term)
    return fibonacci_list

num_terms = 10
result    = fibonacci_sequence(num_terms)
print(f"The first {num_terms} terms of the Fibonacci sequence are: {result}")
print("Time Complexity: O(n)")
print('#' * 80)

# Matrix Multiplication using range
# This example performs matrix multiplication for two 2x2 matrices.

matrix1       = [[1, 2], [3, 4]]
matrix2       = [[5, 6], [7, 8]]
result_matrix = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            # print(result_matrix[i][j],"+=", matrix1[i][k],"*",matrix2[k][j])
            result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

print("Matrix Multiplication Result:")
for row in result_matrix:
    print(row)
print("Time Complexity: O(n)")
print('#' * 80)

# Pascal's Triangle using range
# This example prints Pascal's Triangle up to a specified number of rows.
def generate_pascals_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1]  # start in 1
        if i > 0:
            prev_row = triangle[-1]
            # print("len",len(prev_row))
            # this code increase across the len right of triangle
            # 1 - loop [1]       - No  accomplish - i == 0
            # 2 - loop [1,1]     - No  accomplish - 1+1  
            # 3 - loop [1,2,1]   - Yes accomplish - 1+2, 2+1 
            # 4 - loop [1,3,3,1] - Yes accomplish - 1+3, 3+3, 3+1 ....
            row.extend(prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1))
            row.append(1)
        triangle.append(row)
    return triangle

# Example usage
num_rows = 6
pascals_triangle = generate_pascals_triangle(num_rows)
for row in pascals_triangle:
    print(" ".join(map(str, row)).center(num_rows * 4))
print("Time Complexity: O(n)")
print('#' * 80)

# Collatz Conjecture using range
# This example demonstrates the Collatz Conjecture sequence for a given starting number.
def collatz_conjecture_sequence(start):
    sequence = [start]
    while start != 1:
        if start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1
        sequence.append(start)
    return sequence

# Example usage
start_number = 10
collatz_sequence = collatz_conjecture_sequence(start_number)
print(f"Collatz sequence starting from {start_number}: {collatz_sequence}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Reversed String using range
# This example reverses a given string using a loop and the range function.

def reverse_string(str):
    reversed_str = ""
    for i in range(len(str)-1, -1, -1): # this reversed the count
        reversed_str += str[i]
    return reversed_str

# Example usage
text = "Hello, World!"
reversed_text = reverse_string(text)
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Character Frequency Counter using range
# This example counts the frequency of characters in a given string.

def count_character_frequency(str):
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage
text = "hello, world"
char_frequency = count_character_frequency(text)
print("Character Frequency:")
for char, freq in char_frequency.items():
    print(f"'{char}' occurs {freq} times.")

print("Time Complexity: O(n^2)")
print('#' * 80)

# Binary Search using range
# This example implements the binary search algorithm to find the index of a target element in a sorted list.
def binary_search(arr, target):
    low, high = 0, len(arr)
    while (low <= high):
        mid = int((high + low)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
sorted_list     = [2, 4, 6, 8, 10, 12, 14, 16, 18]
target_element = 10
result_index = binary_search(sorted_list, target_element)
print(f"Index of {target_element} in the list: {result_index}")
print("Time Complexity: O(log n)")
print('#' * 80)

# Generating Power Sets using range
# This example generates all possible subsets (power sets) of a given set.

def generate_power_sets(input_set):
    power_sets = [[]]
    # Generate all combinations by adding elements from input_set into each subset
    for element in input_set:
        new_sets = [subset + [element] for subset in power_sets]
        power_sets.extend(new_sets)
    return power_sets

# Example usage
input_set = [1, 2, 3]
power_sets = generate_power_sets(input_set)
print(f"Power sets of {input_set}: {power_sets}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Matrix Transposition using range
# This example performs the transposition of a given matrix.

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed
# Example Usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)

print("Time Complexity: O(n^2)")
print('#' * 80)

def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, - shift)

# Example usage
text = "Hello, World!"
shift_value = 3
encrypted_text = caesar_cipher_encrypt(text, shift_value)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)
print(f"Original text: {text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Array Left Rotation using a Loop
# This example performs a left rotation on an array.

def left_rotate_array(arr, num_rotations):
    # 3 | 3 % 5 = 3
    num_rotations %= len(array)
    # print("1", arr[num_rotations:])
    # print("2", arr[:num_rotations])
    rotated_arr    = arr[num_rotations:] + arr[:num_rotations]
    return rotated_arr

# Example usage
array = [1, 2, 3, 4, 5]
rotations = 3
rotated_array = left_rotate_array(array, rotations)
print(f"Original array: {array}")
print(f"Left rotated array: {rotated_array}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Array Search using a Loop
# This example searches for a target element in an array and returns its index using a loop.

def search_element(arr, target):
    for index, num in enumerate(arr):
        if num == target:
            return index
    return -1

# Example usage
array = [10, 20, 30, 40, 50]
target_element = 30
index = search_element(array, target_element)
print(f"Array: {array}")
print(f"Target element {target_element} found at index: {index}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Array Right Shifting using a Loop
# This example performs a right shift on an array.

def right_shift_array(arr, num_shifts):
    num_shifts %= len(arr)
    shifted_arr = arr[-num_shifts:] + arr[:-num_shifts]
    return shifted_arr

# Example usage
array = [1, 2, 3, 4, 5]
shifts = 3
shifted_array = right_shift_array(array, shifts)
print(f"Original array: {array}")
print(f"Right-shifted array: {shifted_array}")
print("Time Complexity: O(n^2)")
print('#' * 80)

# Array Chunking using a Loop
# This example splits an array into chunks of a specified size.

def chunk_array(arr, chunk_size):
    chunked_arr = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    return chunked_arr

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
chunked_array = chunk_array(array, chunk_size)
print(f"Original array: {array}")
print(f"Chunked array: {chunked_array}")
