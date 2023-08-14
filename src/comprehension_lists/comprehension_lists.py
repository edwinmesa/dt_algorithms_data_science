# Flattening a nested list: This code conver a matrix 2D to list
nested_list    = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [element for sublist in nested_list for element in sublist]
# Using List Comprehension to flatten the Nested Lists.
print(f"Flattened List:", flattened_list)
print('#' * 80)


#Filtering even numbers and calculating their squares: This code valide only the even numbers
numbers         = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print("Squared Even:", squared_numbers)
print('#' * 80)

# Operations with Arrays
list1           = [1, 2, 3, 4]
list2           = [5, 6, 7, 8]
# Combined the arrays if x + y is greater than 10
comb_list_10    = [(x, y) for x in list1 for y in list2 if x + y > 10]
print("Combined 10:", comb_list_10)
print('#' * 80)

# Generating a matrix using nested list comprehensions:
matrix          = [[row * col for col in range(1,6)] for row in range(1,6)]
print("Matrix:", matrix)
print('#' * 80)

# Extracting unique characters from a list of strings:
words          = ["hello", "world", "open", "ai"]
unique_chars   = list({char for word in words for char in word})
print("Unique Chars:", unique_chars)
print('#' * 80)

# Generating a list of prime numbers:
def is_prime(n):
    # Is neccesary check if the value is less that 2
    if n < 2:
        return False
    # Otherwise 
    # iterate over all values between 2 and sqrt(number). If any divides it then its not
    for i in range(2, int(n ** 0.5) +1): # i = 2
        if n % 2 == 0:
            return False
    return True

# Given a limit extract the prime values
limit  = 20
# You can pass a function is  a comprehension list: Its Nice!
prime_numbers   = [x for x in range(2, limit) if is_prime(x)]
print("Prime Numbers:", prime_numbers)
print('#' * 80)

# Finding common elements between two lists:
list1           = [1,2,3,4,5]
list2           = [4,5,6,7,8]
common_elements = set([x for x in list1 if x in list2]) # I used to avoid duplicates
print("Common elements:", common_elements)
print('#' * 80)

# Creating a dictionary from two lists:
keys    = ['a', 'b','c','d']
values  = [1, 2, 3, 4]
dict    = {k : v for k, v in zip(keys, values)}
print('Dictionary:', dict)
print('#' * 80)

# Finding all anagrams in a list of words:
words           = ["pol","lop","edw","plo","dre","pli","der","red"] 
anagrams        = [word for word in words if sorted(word) == sorted(words[0])] # Use sorted to compare and evaluated
print("Anagrams:", anagrams)
print('#' * 80)

# Creating a matrix transpose using nested list comprehensions:
matrix          = [[10,15,20],[25,30,40],[40,60,90],[90,35,58]]
traspose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Traspose Matrix", traspose_matrix)
print('#' * 80)

# Extracting unique words from a list of sentences:
sentences       = ["I love Caroline is wonderfull", "the life is great", "python is great"]
unique_words    = list({word for sentence in sentences for word in sentence.split()})
print("Unique Words:", unique_words)
print('#' * 80)

# Converting a list of strings to uppercase, excluding strings starting with a vowel:
strings         = ["apple", "banana", "Orange", "kiwi", "pear"]
upper_str       = [string.upper() for string in strings if not string.lower().startswith(('a','e','i','o','u'))]
print("Upper Case:", upper_str)
print('#' * 80)

# Replacing negative numbers with zero:
nums            = [1,-2,-3,-4, 5]
non_negatives   = [num if num >= 0 else 0 for num in nums]
print(non_negatives)
print('#' * 80)

# Comparing elements in two lists and performing operations:
list1               = [1, 2, 3, 4, 5]
list2               = [3, 4, 5, 6, 7]
greater_than_list_2 = [x for x in list1 if any(x > y for y in list2)]
print(greater_than_list_2)
# Output: [4, 5]
print('#' * 80)

# Applying a function to elements and replacing them
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(num) for num in numbers]
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]
