# # Get user input
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# confirmation_password = input("Confirm your password: ")

# # Initialize flags
# has_at = False
# has_dot = False
# at_found = False
# last_dot_index = -1

# # Check email format manually
# i = 0
# while i < len(email):
#     char = email[i]
    
#     if char == '@':
#         has_at = True
#         at_found = True
#         # Ensure there is at least one character before '@'
#         if i == 0:
#             has_at = False
#     elif char == '.':
#         if at_found:
#             has_dot = True
#             last_dot_index = i
    
#     i += 1

# # Check domain part length after the last '.'
# domain_length_valid = False
# if has_at and has_dot and last_dot_index != -1:
#     domain_part_length = len(email) - last_dot_index - 1
#     if domain_part_length >= 2:
#         domain_length_valid = True

# # Validate email and password
# if has_at and has_dot and domain_length_valid:
#     # Check if password and confirmation password match
#     if password == confirmation_password:
#         print("User credentials are valid.")
#     else:
#         print("Passwords do not match.")
# else:
#     print("Invalid email format.")



# # Allow up to 3 attempts
# attempts = 3
# valid_credentials = False

# while attempts > 0 and not valid_credentials:
#     # Get user input
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
#     confirmation_password = input("Confirm your password: ")

#     # Initialize flags
#     has_at = False
#     has_dot = False
#     at_found = False
#     last_dot_index = -1

#     # Check email format manually
#     i = 0
#     while i < len(email):
#         char = email[i]
        
#         if char == '@':
#             has_at = True
#             at_found = True
#             # Ensure there is at least one character before '@'
#             if i == 0:
#                 has_at = False
#         elif char == '.':
#             if at_found:
#                 has_dot = True
#                 last_dot_index = i
        
#         i += 1
    
#     # Check domain part length after the last '.'
#     domain_length_valid = False
#     if has_at and has_dot and last_dot_index != -1:
#         domain_part_length = len(email) - last_dot_index - 1
#         if domain_part_length >= 2:
#             domain_length_valid = True

#     # Validate email and password
#     if has_at and has_dot and domain_length_valid and (password == confirmation_password):
#         valid_credentials = True
#         print("User credentials are valid.")
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(f"Invalid credentials. You have {attempts} attempt(s) left.")
#         else:
#             print("Failed to provide valid credentials after 3 attempts.")



# Maximum number of attempts
max_attempts = 3

# Get user input for email only once
email = input("Enter your email: ")

# Initialize flag for credential validity
valid_credentials = False

# Store the first password entered
first_password = None

# Initialize attempt counter
attempt = 0

# Loop for up to 3 attempts for password and confirmation password
while attempt < max_attempts:
    # Get user input for password and confirmation password
    password = input("Enter your password: ")
    confirmation_password = input("Confirm your password: ")

    # Initialize flags for email validation
    has_at = False
    has_dot = False
    at_found = False
    last_dot_index = -1

    # Check email format manually
    for i in range(len(email)):
        char = email[i]
        
        if char == '@':
            has_at = True
            at_found = True
            # Ensure there is at least one character before '@'
            if i == 0:
                has_at = False
        elif char == '.':
            if at_found:
                has_dot = True
                last_dot_index = i

    # Check domain part length after the last '.'
    domain_length_valid = False
    if has_at and has_dot and last_dot_index != -1:
        domain_part_length = len(email) - last_dot_index - 1
        if domain_part_length >= 2:
            domain_length_valid = True

    # Handle first password entry
    if attempt == 0:
        first_password = password

    # Validate email and passwords
    if has_at and has_dot and domain_length_valid and (password == confirmation_password):
        if attempt > 0 and password != first_password:
            print(f"Password does not match the first password.")
        else:
            valid_credentials = True
            print("User credentials are valid.")
            break
    else:
        attempts_left = max_attempts - (attempt + 1)
        if attempts_left > 0:
            print(f"Invalid credentials. You have {attempts_left} attempt(s) left.")
        else:
            print("Failed to provide valid credentials after 3 attempts.")

    # Increment attempt counter
    attempt += 1

# Post-loop action
if not valid_credentials:
    print("Failed to provide valid credentials after 3 attempts.")
