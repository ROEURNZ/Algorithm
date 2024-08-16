# Write the python code to check for the problems

#! 1. count the number of characters in the string

#! A. count the number of characters using for loop "for" iteration and keyword "in"
# string = "Hello World!"
# count = 0
# for char in string:
#     count += 1
# print(count)

#! B. count of characters in string using for loop of index iteration

# count = 0
# for i in range(len(string)):
#     count += 1
# print(count)

#! C. count of characters in string using while loop of index iteration

# count = 0
# i = 0
# while i < len(string):
#     count += 1
#     i += 1

# print(count)

#! 2. check if the string is a palindrome using break statement

#! A. check if string is palindrome using for loop of index iteration

# string = "racecar"

# is_palindrome = True  # Assume the string is a palindrome initially

# for i in range(len(string) // 2):  # Loop only through the first half of the string
#     # if string[i] != string[len(string) - i - 1]:  # Compare characters from both ends
#     if string[i] != string[-(i + 1)]:
#         is_palindrome = False  # Set flag to False if mismatch is found
#         # No break statement, continue to check the rest of the string

# if is_palindrome:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")



#! 3. check string to count consonants and vowel characters

#! A. count consonants and vowels using for loop of index iteration

# string = "Hello World!"

# consonants_count = 0
# vowels_count = 0

# vowels = "aeiouAEIOU"

# for i in range(len(string)):
#     char = string[i]

#     if char.isalpha():
#         if char in vowels:
#             vowels_count += 1
#         else:
#             consonants_count += 1

# print("Number of consonants:", consonants_count)
# print("Number of vowels:", vowels_count)



# string = "Hello World!"

# consonants_count = 0
# vowels_count = 0

# vowels = "aeiouAEIOU"

# for i in range(len(string)):
#     char = string[i]

#     # Check if the character is a letter
#     if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
#         if char in vowels:
#             vowels_count += 1
#         else:
#             consonants_count += 1

# print("Number of consonants:", consonants_count)
# print("Number of vowels:", vowels_count)


#! B. Check duplicate characters


# Create an empty dictionary to store the character count

# char_count = {}

# string = "Hello World!"

# # Dictionary to track character counts
# char_count = {}
# duplicates = []

# # Count occurrences of each character
# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# # Identify duplicates
# for char in char_count:
#     if char_count[char] > 1:
#         duplicates += [char]  # Using list concatenation to add duplicates

# print("Duplicate characters:", duplicates)



#! C. Count duplicates in the original string

# string = "Hello World"

# # Dictionary to track character counts
# char_count = {}

# # Count occurrences of each character
# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# # Print counts for characters that have duplicates
# for char in char_count:
#     if char_count[char] > 1:
#         print(f"'{char}' is {char_count[char]}")


#! D. count the number of characters once per character excluding a whitespace character

# string = "Hello World"

# # List to track unique characters
# unique_characters = []

# # Count occurrences of each character
# for char in string:
#     # Check if the character is a space
#     if char != ' ':
#         # Assume the character is not found
#         found = False
#         for unique_char in unique_characters:
#             if char == unique_char:
#                 found = True
        
#         # If the character was not found in the unique_characters list, add it
#         if not found:
#             unique_characters += [char]

# # Count the number of unique characters
# unique_char_count = len(unique_characters)

# print("Number of unique characters (excluding spaces):", unique_char_count)


#! E. Remove character based on index input


# string = "Hello World" # string   = "Hello World

# # Prompt the user to enter the index of the character to remove

# index = int(input("Enter the index of the character to remove: "))

# # Check if the index is valid

# if 0 <= index < len(string):

#     # Remove the character at the given index

#     string = string[:index] + string[index + 1:]

# print("Modified string:", string)


#! F. Remove the character at the given index from the string array

# string_array = ["Hello", "World", "!"]

# # Get the index from user input
# index = int(input("Enter the index of the character to remove: "))

# # Remove character at the given index from each string in the array
# new_string_array = []
# for string in string_array:
#     if 0 <= index < len(string):  # Ensure the index is within the bounds of the string
#         new_string = string[:index] + string[index + 1:]
#         new_string_array.append(new_string)
#     else:
#         # Append the original string if index is out of range
#         new_string_array.append(string)

# print("Updated string array:", new_string_array)


#! G. 