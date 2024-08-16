
"""
 #? What is a string in python program?
 #! In Python, a string is a sequence of characters enclosed in quotes. Strings can be defined using:
  1. Single Quotes: '...'
  2. Double Quotes: "..."
  3. Triple Quotes: '''...''' 
  4. Strings are used to represent text and can include letters, numbers, symbols, and whitespace.
  
"""
#! 1. String with default values set up

string1 = "Hello"
string2 = "World"

#! 2. Concatenation of two strings separated by spaces using + operator

concatenated_string = string1 + " " + string2
print(concatenated_string)

#! 3. Accessing characters in a string using indexing

# Indexing starts from 0, so the first character is at index 0, the second at index 1, and so on.

first_character = concatenated_string[0]
second_character = concatenated_string[1]

print(f"First character: {first_character}")
print(f"Second character: {second_character}")

#! 4. String slicing

# Slicing allows you to extract a part of a string.

# Syntax: string[start:end:step]

# By default, start is 0, end is the length of the string, and step is 1.

# Slicing a string with no start or end value defaults to the entire string.

sliced_string = concatenated_string[:]

print(f"Sliced string: {sliced_string}")


#! 5. numbers of characters in a string

# len() function returns the number of characters in a string.

number_of_characters = len(concatenated_string)

print(f"Number of characters in '{concatenated_string}' are {number_of_characters}.")

#! 6. String methods

# Some common string methods in Python include:

# 1. capitalize() - Converts the first character to uppercase and the rest to lowercase.

capitalized_string = concatenated_string.capitalize()
print(f"Capitalized string: {capitalized_string}")

# 2. uppercase() and lowercase() of the string

uppercase_string = concatenated_string.upper()
lowercase_string = concatenated_string.lower()
print(f"Uppercase string: {uppercase_string}")
print(f"Lowercase string: {lowercase_string}")

# 3. check type of string gidit or character

is_gidit = string2.isdigit()
is_character = string1.isalpha()
print(f"Is the string a digit? {is_gidit}")
print(f"Is the string a character? {is_character}")

# 4. check character consist in string

is_character_in_string = "o" in concatenated_string

print(f"Is 'o' in the string? {is_character_in_string}")