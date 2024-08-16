def process_and_insert(array, target):

    new_array = []

    # Iterate through the range from 1 to range_end (inclusive)
    for i in range(1, (len(array)+target) + 1):
        # Add each number to the new_array
        new_array += [i]

    return new_array

def parse_input(input_number):

    array = []
    num_str = ''

    for char in input_number:
        if char == '[' or char == ']':
            # Skip brackets
            pass
        elif char == ',':
            # Convert num_str to integer if it's not empty
            if num_str != '':
                array += [int(num_str)]
                num_str = ''  # Reset num_str
        else:
            # Accumulate characters for num_str
            num_str += char
    
    # Convert the last number if num_str is not empty
    if num_str != '':
        array += [int(num_str)]
    
    return array

# Get user input for the array
input_number = int(input("Enter the array elements as a number [1,3,5,7,9]: "))

# Parse the input string to get the array
array = parse_input(input_number)

# Set the target value (default is 2)
target = 2

# Generate the complete list
result = process_and_insert(array, target)
print("Resulting array:", result)
 # type: ignore