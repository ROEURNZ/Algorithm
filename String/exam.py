
# def insert_in_order(array, target, index):
#     """
#     Insert the target number into the array at the specified index using slicing and a for loop.
    
#     Parameters:
#     array (list): The original array of numbers.
#     target (int): The target number to insert.
#     index (int): The index at which to insert the target number.
    
#     Returns:
#     list: The modified array after inserting the target number.
#     """
#     # Initialize an empty list for the new array
#     new_array = []
    
#     # Add elements from the original array before the index
#     for i in range(index):
#         new_array += [array[i]]
    
#     # Insert the target at the specified index
#     new_array += [target]
    
#     # Add the remaining elements from the original array after the index
#     for i in range(index, len(array)):
#         new_array += [array[i]]
    
#     return new_array

# # Example usage:
# array = [1, 3, 5, 7, 9]
# target = 2
# index = 1

# # Insert the target number into the array
# result = insert_in_order(array, target, index)
# print("Resulting array:", result)




