# def add_binary(bin1, bin2):
#     """Add two binary strings."""
#     # Ensure both binary strings are of the same length
#     len1, len2 = len(bin1), len(bin2)
#     if len1 < len2:
#         bin1 = '0' * (len2 - len1) + bin1
#     elif len2 < len1:
#         bin2 = '0' * (len1 - len2) + bin2

#     result = ''
#     carry = 0

#     # Add binary numbers from the end to the beginning
#     for i in range(len(bin1) - 1, -1, -1):
#         bit_sum = int(bin1[i]) + int(bin2[i]) + carry
#         if bit_sum == 0:
#             result = '0' + result
#             carry = 0
#         elif bit_sum == 1:
#             result = '1' + result
#             carry = 0
#         elif bit_sum == 2:
#             result = '0' + result
#             carry = 1
#         elif bit_sum == 3:
#             result = '1' + result
#             carry = 1

#     if carry:
#         result = '1' + result

#     return result

# def subtract_binary(bin1, bin2):
#     """Subtract two binary strings (bin1 - bin2)."""
#     # Ensure both binary strings are of the same length
#     len1, len2 = len(bin1), len(bin2)
#     if len1 < len2:
#         bin1 = '0' * (len2 - len1) + bin1
#     elif len2 < len1:
#         bin2 = '0' * (len1 - len2) + bin2

#     result = ''
#     borrow = 0

#     # Subtract binary numbers from the end to the beginning
#     for i in range(len(bin1) - 1, -1, -1):
#         bit_diff = int(bin1[i]) - int(bin2[i]) - borrow
#         if bit_diff == 0:
#             result = '0' + result
#             borrow = 0
#         elif bit_diff == 1:
#             result = '1' + result
#             borrow = 0
#         elif bit_diff == -1:
#             result = '1' + result
#             borrow = 1
#         elif bit_diff == -2:
#             result = '0' + result
#             borrow = 1

#     # Remove leading zeros from the result
#     return result.lstrip('0') or '0'

# def evaluate_binary_expression(expression):
#     """Evaluate a binary expression with + and - operators."""
#     tokens = expression.split()
#     result = tokens[0]

#     i = 1
#     while i < len(tokens):
#         operator = tokens[i]
#         next_number = tokens[i + 1]

#         if operator == '+':
#             result = add_binary(result, next_number)
#         elif operator == '-':
#             result = subtract_binary(result, next_number)

#         i += 2

#     return result

# # Example usage:
# expression = input("Enter a binary expression (e.g., 1010 + 1101 - 1001): ")
# result = evaluate_binary_expression(expression)
# print(f"The result of the binary expression is {result}")





def add_binary(bin1, bin2):
    """Add two binary strings."""
    len1, len2 = len(bin1), len(bin2)
    if len1 < len2:
        bin1 = '0' * (len2 - len1) + bin1
    elif len2 < len1:
        bin2 = '0' * (len1 - len2) + bin2

    result = ''
    carry = 0

    for i in range(len(bin1) - 1, -1, -1):
        bit_sum = int(bin1[i]) + int(bin2[i]) + carry
        if bit_sum == 0:
            result = '0' + result
            carry = 0
        elif bit_sum == 1:
            result = '1' + result
            carry = 0
        elif bit_sum == 2:
            result = '0' + result
            carry = 1
        elif bit_sum == 3:
            result = '1' + result
            carry = 1

    if carry:
        result = '1' + result

    return result

def subtract_binary(bin1, bin2):
    """Subtract two binary strings (bin1 - bin2)."""
    len1, len2 = len(bin1), len(bin2)
    if len1 < len2:
        bin1 = '0' * (len2 - len1) + bin1
    elif len2 < len1:
        bin2 = '0' * (len1 - len2) + bin2

    result = ''
    borrow = 0

    for i in range(len(bin1) - 1, -1, -1):
        bit_diff = int(bin1[i]) - int(bin2[i]) - borrow
        if bit_diff == 0:
            result = '0' + result
            borrow = 0
        elif bit_diff == 1:
            result = '1' + result
            borrow = 0
        elif bit_diff == -1:
            result = '1' + result
            borrow = 1
        elif bit_diff == -2:
            result = '0' + result
            borrow = 1

    return result.lstrip('0') or '0'

def evaluate_binary_expression(expression_parts):
    """Evaluate a binary expression with + and - operators."""
    if not expression_parts:
        return '0'

    result = expression_parts[0]

    for i in range(1, len(expression_parts), 2):
        operator = expression_parts[i]
        next_number = expression_parts[i + 1]

        if operator == '+':
            result = add_binary(result, next_number)
        elif operator == '-':
            result = subtract_binary(result, next_number)

    return result

def main():
    expression_parts = [None] * 100  # Arbitrary large list to hold inputs
    index = 0
    print("Enter binary numbers and operators. Type '=' to calculate the result.")

    while True:
        user_input = input("Enter binary number/operator: ")
        
        if user_input == '=':
            # Calculate and format the result
            result = evaluate_binary_expression(expression_parts[:index])
            # Manually construct the expression string
            expression = ""
            for i in range(index):
                if i > 0:
                    expression += " " + expression_parts[i]
                else:
                    expression = expression_parts[i]
            print(f"The result of the binary expression {expression} = {result}")
            return  # Exit the function, effectively ending the program
        else:
            expression_parts[index] = user_input
            index += 1

if __name__ == "__main__":
    main()
