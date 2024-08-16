# Write the unordered sequence 
# 1. array of integers [1, 4, 3, 6, 2, 8, 11, 0]
# find the minimum and maximum values of the sequence without the def function

# # Array of integers
# array = [1, 4, 3, 6, 2, 8, 11, 0]

# # Initialize min_value and max_value to the first element of the array
# min_value = array[0]
# max_value = array[0]

# # Iterate through the array to find the minimum and maximum values
# for i in array:
#     if i < min_value:
#         min_value = i
#     elif i > max_value:
#         max_value = i

# # Print the results
# print("Minimum value is", min_value,"and maximum value is", max_value)


# 2. Modulus of the number of n + 1 n is real numbers, n is even number

# Input: an even real number n
n = float(input("Enter an even real number: "))

# Check if n is an even integer (this check is usually for integer values)
if n % 2 != 0:
    print("The number is not even.")
else:
    # Compute n + 1
    result = n + 1
    
    # Compute the modulus of the result without using abs()
    if result < 0:
        modulus = -result
    else:
        modulus = result
    
    # Print the result and its modulus
    print("Result of n + 1:", result)
    print("Modulus of n + 1:", modulus)
