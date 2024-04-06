#!/usr/bin/env python
# coding: utf-8

# # Question#1

# In[2]:


def replace_chars(text):
 for char in [' ', ',', '.']:
     text = text.replace(char, ':')
 return text

sample_text = 'Python Exercises, PHP exercises.'
result = replace_chars(sample_text)
print(result)


# # Question#2

# In[3]:


import pandas as pd
import re

data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)

# Function to remove everything except words
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

# Apply the function to the 'SUMMARY' column
df['SUMMARY'] = df['SUMMARY'].apply(remove_punctuation)

print(df)


# # Question#3

# In[6]:


import re

def find_long_words(text):
    pattern = re.compile(r'\b\w{4,}\b')
    return pattern.findall(text)

text = "This is a sample text with some long words like Python, programming, and computer."
long_words = find_long_words(text)
print(long_words)


# # Question#4

# In[8]:


import re

def find_specific_length_words(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    return pattern.findall(text)

text = "This is a sample text with some words of various lengths like cat, dog, house, and apple."
specific_length_words = find_specific_length_words(text)
print(specific_length_words)


# # Question 5

# In[9]:


import re

def remove_parentheses(strings):
    pattern = re.compile(r'\([^)]*\)')
    return [pattern.sub('', s).strip() for s in strings]

sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
output = remove_parentheses(sample_text)
for item in output:
    print(item)


# # Question 6

# In[37]:


import pandas as pd

def remove_parentheses(text):
    pattern = re.compile(r'\([^)]*\)')
    return pattern.sub('', text).strip()


with open('coding.txt', 'r') as file:
    lines = file.readlines()

modified_lines = [remove_parentheses(line) for line in lines]


with open('output.txt', 'w') as file:
    for line in modified_lines:
        file.write(line + '\n')

print("Output has been written to 'output.txt'.")


# # Question 7

# In[13]:


import re

sample_text = "ImportanceOfRegularExpressionsInPython"

pattern = re.compile(r'[A-Z][a-z]*')

result = pattern.findall(sample_text)

print(result)


# # Question 8

# In[16]:


# import re

def insert_spaces(text):
    result = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
    return result


sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

output = insert_spaces(sample_text)
print(output)


# # Question 9

# In[15]:


import re

def insert_spaces(text):
    result = re.sub(r'(?<=[A-Z0-9])(?=[A-Z][a-z])|(?<=[0-9])(?=[A-Za-z])', ' ', text)
    return result


sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

output = insert_spaces(sample_text)
print(output)


# # Question 10

# [Link to My Code on GitHub](https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv)

# In[42]:


import pandas as pd

github_link = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(github_link)

df['first_five_letters'] = df['Country'].str[:5]

print(df)


# # Question 11

# In[20]:


def match_string(text):
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
    for char in text:
        if char not in allowed_characters:
            return False
    return True


sample_strings = ["Hello123", "world", "Python_123", "!!!", "hello_world"]
for string in sample_strings:
    if match_string(string):
        print(f"{string}: Matches")
    else:
        print(f"{string}: Does not match")


# # Question 12

# In[21]:


def starts_with_number(string, number):
    number_str = str(number)

    if string.startswith(number_str):
        return True
    else:
        return False

test_string = "123abc"
test_number = 123

if starts_with_number(test_string, test_number):
    print(f"The string '{test_string}' starts with the number {test_number}.")
else:
    print(f"The string '{test_string}' does not start with the number {test_number}.")


# # Question 13

# In[22]:


def remove_leading_zeros(ip_address):
    
    octets = ip_address.split('.')
    
    octets = [str(int(octet)) for octet in octets]

    new_ip_address = '.'.join(octets)

    return new_ip_address

ip_address = "192.168.001.001"
new_ip_address = remove_leading_zeros(ip_address)
print("Original IP Address:", ip_address)
print("IP Address without Leading Zeros:", new_ip_address)


# # Question 14

# In[41]:


import re

def find_dates_in_file(file_path):
        # Regular expression pattern for matching dates
        pattern = re.compile(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b')

        # Open the file and read its contents
        with open(file_path, 'r') as file:
            text = file.read()

        # Find the first occurrence of the pattern in the text
        match = pattern.search(text)
        if match:
            return match.group(0)
        else:
            return "Date not found in the file."

    # Example usage:
file_path = 'question.txt'  # Replace 'sample_text.txt' with the path to your text file
date_found = find_dates_in_file(file_path)
print("Date found in the file:", date_found)


# # Question 15

# In[26]:


def search_words(sample_text, searched_words):
    found_words = []
    for word in searched_words:
        if word in sample_text:
            found_words.append(word)
    return found_words

# Sample text
sample_text = 'The quick brown fox jumps over the lazy dog.'

# Searched words
searched_words = ['fox', 'dog', 'horse']

# Search for the words in the sample text
found_words = search_words(sample_text, searched_words)

# Print the found words
print("Found words:", found_words)


# # Question 16

# In[27]:


def search_word_with_location(sample_text, searched_word):
    location = sample_text.find(searched_word)
    return location

sample_text = 'The quick brown fox jumps over the lazy dog.'


searched_word = 'fox'


location = search_word_with_location(sample_text, searched_word)


if location != -1:
    print(f"'{searched_word}' found at index {location} in the sample text.")
else:
    print(f"'{searched_word}' not found in the sample text.")


# # Question17

# In[28]:


def find_substrings(sample_text, pattern):
    positions = []
    start = sample_text.find(pattern)
    while start != -1:
        positions.append(start)
        start = sample_text.find(pattern, start + 1)
    return positions

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

positions = find_substrings(sample_text, pattern)

print("Positions of substrings:", positions)


# # Question 18

# In[29]:


def find_occurrences(sample_text, pattern):
    occurrences = []
    start = 0
    while True:
        start = sample_text.find(pattern, start)
        if start == -1:
            break
        occurrences.append((pattern, start))
        start += 1
    return occurrences


sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'


results = find_occurrences(sample_text, pattern)


for result in results:
    print(f"'{result[0]}' found at position {result[1]}")


# # Question 19

# In[30]:


from datetime import datetime

def convert_date(date_str):
    # Parse the date string in yyyy-mm-dd format
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    # Format the date in dd-mm-yyyy format
    formatted_date = date_obj.strftime('%d-%m-%Y')

    return formatted_date

date_str = '2023-04-12'
converted_date = convert_date(date_str)
print("Original Date:", date_str)
print("Converted Date:", converted_date)


# # Question 20

# In[33]:


import re

def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    return pattern.findall(text)

user_input = input("Enter a string containing decimal numbers: ")

decimal_numbers = find_decimal_numbers(user_input)

print("Decimal numbers with precision of 1 or 2:", decimal_numbers)


# # Question 21

# In[37]:


def separate_numbers_and_positions(input_string):
    numbers_and_positions = []
    for i, char in enumerate(input_string):
        if char.isdigit():
            numbers_and_positions.append((char, i))
    return numbers_and_positions

input_string = "Hello123World456"
result = separate_numbers_and_positions(input_string)
print("Numbers and their positions:", result)


# # Question 22

# In[38]:


import re

def extract_maximum_numeric_value(text):
    
    pattern = re.compile(r'\b\d+\b')

    numeric_values = [int(match) for match in pattern.findall(text)]

    max_value = max(numeric_values)

    return max_value


sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'


max_numeric_value = extract_maximum_numeric_value(sample_text)

print("Maximum numeric value:", max_numeric_value)


# # Question 23

# In[39]:


import re

def insert_spaces(text):
    # Use regular expression to insert spaces before words starting with capital letters
    result = re.sub(r'([A-Z][a-z]+)', r' \1', text)
    return result.strip()  # Strip leading and trailing spaces

# Sample text
sample_text = "RegularExpressionIsAnImportantTopicInPython"

# Call the function and print the output
output = insert_spaces(sample_text)
print(output)


# # Question 24

# In[40]:


import re

def find_upper_lower_sequences(text):
    pattern = re.compile(r'[A-Z][a-z]+')
    sequences = pattern.findall(text)
    return sequences

# Test the function
sample_text = "The Quick Brown Fox Jumps Over The Lazy Dog"
result = find_upper_lower_sequences(sample_text)
print("Sequences of one upper case letter followed by lower case letters:")
print(result)


# # Question 25

# In[41]:


def remove_continuous_duplicates(sentence):
    words = sentence.split()
    result = [words[0]]  # Initialize the result with the first word
    for i in range(1, len(words)):
        # If the current word is different from the previous word, add it to the result
        if words[i] != words[i - 1]:
            result.append(words[i])
    return ' '.join(result)

# Test the function
sample_text = "Hello hello world world"
output = remove_continuous_duplicates(sample_text)
print("Result:", output)


# In[ ]:




