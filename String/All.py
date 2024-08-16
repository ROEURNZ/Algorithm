# def indexes(string, substring):
#     l = []
#     length = len(string)
#     index = 0
#     while index < length:
#         i = string.find(substring, index)
#         if i == -1:
#             return l
#         l.append(i)
#         index = i + 1
#     return l
# s = "substring in python"
# print(indexes(s, 'i'))

# Rewrite the code above without using def functions

# no def function

# s = input("substring in python: ")
# substring = 'i'
# l = []
# substring_length = len(substring)

# for i in range(len(s) - substring_length + 1):
#     if s[i:i + substring_length] == substring:
#         l += [i]  # Concatenating the list with a new list containing the index

# print(l)



string = "substring in python format"
substring = input("character of string: ")
l = []
substring_length = len(substring)

for i in range(len(string) - substring_length + 1):
    match = True
    for j in range(substring_length):
        if string[i + j] != substring[j]:
            match = False
    if match:
        l += [i]  # Concatenating the list with a new list containing the index

print(l)

