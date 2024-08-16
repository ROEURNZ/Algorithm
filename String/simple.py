# def generate_full_range(input_list):
#     # Determine the starting and ending points of the range
#     start = input_list[0]
#     end = input_list[-1]
    
#     # Initialize an empty list for the range
#     range_list = []
    
#     # Fill the range_list with numbers from start to end
#     for i in range(start, end + 1):
#         range_list = range_list + [i]
    
#     return range_list

# # Prompt the user to enter the number of elements
# num_elements = int(input("How many numbers will you enter? "))

# # Initialize an empty list to collect the numbers
# input_list = []

# # Collect the numbers from the user
# for _ in range(num_elements):
#     number = int(input("Enter a number: "))
#     input_list = input_list + [number]

# # Generate the full range based on the user's input
# result = generate_full_range(input_list)
# print(result)

# Write


def generate_full_range(input_list):
    # Determine the starting and ending points of the range
    start = input_list[0]
    end = input_list[-1]
    
    # Initialize an empty list for the range
    range_list = []
    
    # Fill the range_list with numbers from start to end
    for i in range(start, end + 1):
        range_list = range_list + [i]
    
    return range_list

def sum_of_array(array):
    # Initialize sum
    total_sum = 0
    
    # Sum up all elements in the array
    for number in array:
        total_sum += number
    
    return total_sum

# Prompt the user to enter the number of elements
num_elements = int(input("How many numbers will you enter? "))

# Initialize an empty list to collect the numbers
input_list = []

# Collect the numbers from the user
for _ in range(num_elements):
    number = int(input("Enter a number: "))
    input_list = input_list + [number]

# Generate the full range based on the user's input
result = generate_full_range(input_list)
print("Generated range:", result)

# Calculate the sum of the generated range
total_sum = sum_of_array(result)
print("Sum of the range:", total_sum)
