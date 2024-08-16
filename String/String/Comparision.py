
# A. Compare the two strings lengths

# Get two strings from user input
# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")

# # Compare the lengths
# if len(s1) == len(s2):
#     print("The two strings have the same length.")
# elif len(s1) < len(s2):
#     print("The first string is shorter than the second string.")
# else:
#     print("The first string is longer than the second string.")






# Get two strings from user input
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Get the lengths of the strings
len_s1 = len(s1)
len_s2 = len(s2)

# Compare the lengths
if len_s1 == len_s2:
    print("The two strings have the same length.")
else:
    if len_s1 < len_s2:
        print("The first string is shorter than the second string.")
    else:
        print("The first string is longer than the second string.")

# Compare the strings character by character if they are of the same length
if len_s1 == len_s2:
    if s1 == s2:
        print("The two strings are identical.")
    else:
        print("The two strings have the same length but are different.")



#! User credentials input, email, password and confirmation password
