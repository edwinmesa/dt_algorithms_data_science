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
print("replacing negatives with 0:",non_negatives)
print('#' * 80)

# Comparing elements in two lists and performing operations:
list1               = [1, 2, 3, 4, 5]
list2               = [3, 4, 5, 6, 7]
greater_than_list_2 = [x for x in list1 if any(x > y for y in list2)]
print("comparing values:",greater_than_list_2)
# Output: [4, 5]
print('#' * 80)

# Applying a function to elements and replacing them
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(num) for num in numbers]
print("squared nums:",squared_numbers)
# Output: [1, 4, 9, 16, 25]
print('#' * 80)

import pandas as pd

# Create a sample dataframe
data = {'First Name': ['Alice', 'Bob', 'Charlie','Kila', 'Pola', 'Caro'],
        'Last Name': ['Key', 'Kloi', 'Brown','Key', 'Kloi', 'Brown'],
        'Email': ['Key@ki.com', 'Kloi@lo.com', 'Brown@gmail.com','Key@hotmail.com', 'Kloi@yahoo.es', 'Brown@pola.com'],
        'Value':[115, 90, 85, 100, 105, 95],
        'Sales':[1200, 900, 850, 1000, 1050, 950],
        'Profit':[250, 300, 150, 260, 400, 300],
        'Daily Sales':[30, 45, 70, 60, 15, 20],
        'Age': [25, 30, 22, 10, 80, 5],
        'Income': [100,70,90,50,30,98],
        'Birthdate': ['1990-05-15', '1998-08-20', '1992-03-10','2005-05-15', '2018-08-20', '2012-03-10'],
        'Hobby 1': ['Video Games', 'Music', 'Soccer', 'Music', 'Drive', 'Sing'],
        'Hobby 2': ['Music', 'TV Shows', 'Soccer', 'Sing', 'Music', 'Drive'],
        'Gender':['Female','Male','Male','Female','Male','Male']
        }
df = pd.DataFrame(data)

# Use a list comprehension to create a new column 'AgePlusOne' by adding 1 to each age
df['AgePlusOne'] = [age + 1 for age in df['Age']]

print(df)
print('#' * 80)
df['AgeSquared'] = [age**2 for age in df['Age']]
print(df)
print('#' * 80)
df['Gender'] = [1 if gender == 'Male' else 0 for gender in df['Gender']]
print(df)
print('#' * 80)
df['Category'] = ['Young' if age < 30 else 'Middle-aged' if age < 50 else 'Senior' for age in df['Age']]
print(df)
print('#' * 80)
df['Full Name'] = [f"{first} {last}" for first, last in zip(df['First Name'], df['Last Name'])]
print(df)
print('#' * 80)
age_bins = [0, 18, 30, 50, float('inf')]
age_labels = ['Child', 'Young Adult', 'Adult', 'Senior']
df['Age Group'] = [age_labels[i] for i in pd.cut(df['Age'], bins=age_bins, labels=age_labels).cat.codes]
print(df)
print('#' * 80)
mean_value = df['Value'].mean()
df['Squared Difference'] = [(value - mean_value)**2 for value in df['Value']]
print(df)
print('#' * 80)
hobbies = [hobby for sublist in df[['Hobby 1', 'Hobby 2']].values for hobby in sublist if pd.notna(hobby)]
print(df)
print('#' * 80)
import pandas as pd
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-01-10')
date_range = [start_date + pd.DateOffset(days=i) for i in range((end_date - start_date).days + 1)]
date_df = pd.DataFrame({'Date': date_range})
print(date_df)
print('#' * 80)
min_income = df['Income'].min()
max_income = df['Income'].max()
df['Normalized Income'] = [(income - min_income) / (max_income - min_income) for income in df['Income']]
print(df)
print('#' * 80)
from datetime import datetime
today = datetime.today()
df['Birthdate'] = pd.to_datetime(df['Birthdate'])
df['Age'] = [(today - birthdate).days // 365 for birthdate in df['Birthdate']]
print(df)
print('#' * 80)
mean_sales = df['Sales'].mean()
df['Profit'] = [profit * 2 if sales > mean_sales else profit for sales, profit in zip(df['Sales'], df['Profit'])]
print(df)
print('#' * 80)
df['Email Domain'] = [email.split('@')[1] for email in df['Email']]
print(df)
print('#' * 80)
window_size = 7
df['7-Day Rolling Avg'] = [df['Daily Sales'][i:i+window_size].mean() if i + window_size <= len(df) else None for i in range(len(df))]
print(df)
print('#' * 80)