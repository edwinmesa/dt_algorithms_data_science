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