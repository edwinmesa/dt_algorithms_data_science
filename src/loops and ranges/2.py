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
            