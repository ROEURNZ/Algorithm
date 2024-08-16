# def length_of_longest_substring(s):
#     # Create a dictionary to store the last index of each character
#     char_index_map = {}
#     start = 0  # Start index of the current window
#     max_length = 0  # Maximum length of substring found
    
#     for end in range(len(s)):
#         char = s[end]
        
#         if char in char_index_map:
#             last_index = char_index_map[char]
            
#             if last_index >= start:
#                 # Move the start to the right of the last occurrence of the current character
#                 start = last_index + 1
        
#         # Update the last index of the current character
#         char_index_map[char] = end
        
#         # Update the maximum length of the substring found without using max()
#         current_length = end - start + 1
#         if current_length > max_length:
#             max_length = current_length

#     return max_length

# # Read the input string from the user
# s = input("Enter the string: ")
# print(length_of_longest_substring(s))









def length_of_longest_substring(s):
    # Define the alphabet as a list of characters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Create an array to store the last index of each character
    char_index = [-1] * len(alphabet)
    
    start = 0  # Start index of the current window
    max_length = 0  # Maximum length of substring found

    for end in range(len(s)):
        char = s[end]
        
        # Determine the index for the character in the alphabet list
        index = -1
        for i in range(len(alphabet)):
            if char == alphabet[i]:
                index = i
                # We found the index, no need to continue searching
                i = len(alphabet)  # Exiting the loop by setting i to an invalid value
        
        # Ensure the character was found and its index is valid
        if index != -1 and char_index[index] >= start:
            # Move the start to the right of the last occurrence of the current character
            start = char_index[index] + 1
        
        # Update the last index of the current character
        char_index[index] = end
        
        # Update the maximum length of the substring found without using max()
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length

    return max_length

# Read the input string from the user
s = input("Enter the string: ")
print(length_of_longest_substring(s))









#! 4. check if the string is a valid palindrome with special characters and spaces

#! A. check if string is palindrome using for loop of index iteration


string = "A man, a plan, a canal: Panama"

is_palindrome = True  # Assume the string is a palindrome initially

string = string.lower()  # Convert string to lowercase for case-insensitive comparison

for i in range(len(string) // 2):  # Loop only through the first half of the string

    # Remove non-alphanumeric characters and spaces

    if string[i]!= string[len(string) - i - 1]:  # Compare characters from both ends

    # if string[i].isalnum() and string[-(i + 1)].isalnum() and string[i]!= string[-(i + 1)]:

        is_palindrome = False  # Set flag to False if mismatch is found

        # No break statement, continue to check the rest of the string


if is_palindrome:

    print("The string is a valid palindrome.")

else:

    print("The string is not a valid palindrome.")

