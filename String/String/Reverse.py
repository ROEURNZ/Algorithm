# Reverse the order of the elements in the list

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Loop to reverse the list
# for i in range(len(list) // 2):
#     # Swap the elements
#     list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]

# print(list)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reverse the list using a for loop and the + operator
reversed_list = []
for i in range(len(list) - 1, -1, -1):
    
    # reversed_list.append(list[i])
    reversed_list += [list[i]] 

print(reversed_list)
