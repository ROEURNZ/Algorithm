# Getting Started with Python

## I. Python Environment Setup

## 1. Setting Up Code or Text Editors

## Visual Studio Code (VS Code):
- Download & Install VS Code
  URL: https://code.visualstudio.com/
- Install Extensions:
  - Python Extension: Search for "Python" in the Extensions view and install the Python extension by Microsoft.
  - Pylint: Install Pylint for linting Python code.

## Visual Studio (Full IDE):
- Download & Install Visual Studio
  URL: https://visualstudio.microsoft.com/
- Install Workloads:
  - Select "Python development" during installation.

## 2. Download & Install Python
- Download Python: Go to the official Python website.
  URL: https://www.python.org/downloads/
- Install Python:
  - Follow the installation instructions, ensuring that "Add Python to PATH" is selected during installation.

## 3. Install Required Python Packages

- Open your terminal or command prompt.
- Install commonly used packages:
  
```bash
  - pip install pylint
  - pip install virtualenv
```
### Visual Studio:
- The necessary extensions and tools should be included in the installation if you selected the appropriate workloads.

## 4. Getting Started with a Small Project

# Write logic and Algorithm code in python without defining functions

### Exercise 1: Basic String Operations:


- **A. Length of a string:**:
```python
    string = input("Enter the string" )
    length = 0
    for _ in string:
        length += 1
    print(length)
```
- **B. Reverse a string:**:

```python
    string = input("Enter the string" )
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    print(reversed_string)

```
- **C. Concatenate two strings:**
```python
    string1 = input("Enter the string" )
    string2 = input("Enter the string" )

    concatenated = ""
    for char in string1:
        concatenated += char
    for char in string2:
        concatenated += char
    print(concatenated)

```
- **D. Count vowels in a string:**
```python
    string = input("Enter the string" )
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    print(vowel_count)
```
- **E. Count consonants in a string:**
```python
    string = input("Enter the string" )

    vowels = "aeiouAEIOU"
    consonant_count = 0
    for char in string:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    print(consonant_count)
```


### Exercise 2: Substring Identification

- **A. Check if a substring exists**:
```python
    string = "hello"
    substring = "ell"
    found = False

    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            found = True

    print(found)
```

- **B. First occurrence of a substring:**:

```python
    string = "hello"
    substring = "ell"
    index = -1

    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            index = i

    print(index)


```
- **C. Last occurrence of a substring:**
```python
    string = "hello"
    substring = "l"
    index = -1
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            index = i
    print(index)
```
- **D. Count how many times a substring appears:**
```python
    string = "hellohello"
    substring = "ell"
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    print(count)
```
- **E. Print all starting indices of a substring:**
```python
    string = "hellohello"
    substring = "ell"
    indices = []
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            indices.append(i)
    print(indices)
```



### Exercise 3: String Modification

- **A. Remove all spaces:**
```python
    string = "hello world"
    no_spaces = ""
    for char in string:
        if char != " ":
            no_spaces += char
    print(no_spaces)
```


- **B. Remove all vowels:**

```python

    string = "hello world"
    vowels = "aeiouAEIOU"
    no_vowels = ""
    for char in string:
        if char not in vowels:
            no_vowels += char
    print(no_vowels)
```

- **C. Replace all occurrences of a substring:**

```python
    string = "hello world"
    old_sub = "l"
    new_sub = "x"
    replaced = ""
    i = 0
    while i < len(string):
        if string[i:i + len(old_sub)] == old_sub:
            replaced += new_sub
            i += len(old_sub)
        else:
            replaced += string[i]
            i += 1
    print(replaced)

```
- **D. Remove a specific substring:**

```python
    string = "hello world"
    substring = "l"
    result = ""
    i = 0
    while i < len(string):
        if string[i:i + len(substring)] == substring:
            i += len(substring)
        else:
            result += string[i]
            i += 1
    print(result)
```
- **E. Remove all instances of the first character:**

```python
    string = "hello"
    first_char = string[0]
    result = ""
    for i in range(1, len(string)):
        if string[i] != first_char:
            result += string[i]
    print(first_char + result)
```

### Exercise 4: Palindromes and Repetition

- **A. Check if a string is a palindrome:**

```python
    string = "racecar"
    is_palindrome = True

    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            is_palindrome = False
            # Use a flag to exit the loop once a mismatch is found
            # The loop will continue but `is_palindrome` will remain `False`

    # Final output based on the flag
    print(is_palindrome)

```

- **B. Check if a substring is repeated consecutively:**

```python
    string = "abcabc"
    substring = "abc"
    is_repeated = True

    # Ensure the length of the string is a multiple of the substring length
    if len(string) % len(substring) != 0:
        is_repeated = False
    else:
        # Check if each segment matches the substring
        for i in range(0, len(string), len(substring)):
            if string[i:i + len(substring)] != substring:
                is_repeated = False

    print(is_repeated)

```

- **C. Longest palindromic substring:**

```python
    string = "babad"
    longest_palindrome = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            sub = string[i:j + 1]
            if sub == sub[::-1] and len(sub) > len(longest_palindrome):
                longest_palindrome = sub
    print(longest_palindrome)
```

- **D. Count occurrences of the first character:**

```python
    string = "hello"
    first_char = string[0]
    count = 0
    for char in string:
        if char == first_char:
            count += 1
    print(count)
```

- **E. Check if all characters are unique:**

```python
    string = "hello"
    unique = True

    for i in range(len(string)):
        found_duplicate = False
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                found_duplicate = True
        if found_duplicate:
            unique = False

    print(unique)
```

### Exercise 5: String and Substring Manipulation

- **A. Remove substring from start and end:**

```python
    string = "abcxyzabc"
    substring = "abc"
    if string.startswith(substring):
        string = string[len(substring):]
    if string.endswith(substring):
        string = string[:-len(substring)]
    print(string)
```

- **B. Extract substring between first and last occurrence of a character:**

```python
    string = "hello world"
    char = "o"
    start = 0
    end = len(string) - 1
    while start < len(string) and string[start] != char:
        start += 1
    while end >= 0 and string[end] != char:
        end -= 1
    if start < end:
        result = string[start + 1:end]
    else:
        result = ""
    print(result)
```

- **C. Print the middle character(s) of a string:**

```python
    string = "hello"
    middle = len(string) // 2
    if len(string) % 2 == 0:
        print(string[middle - 1:middle + 1])
    else:
        print(string[middle])
```

- **D. Swap the first and last characters:**

```python
    string = "hello"
    if len(string) > 1:
        result = string[-1] + string[1:-1] + string[0]
    else:
        result = string
    print(result)
```

- **E. Print every second character:**
  
```python
    string = "hello"
    result = ""
    for i in range(1, len(string), 2):
        result += string[i]
    print(result)
```

### Exercise 6: Substring Patterns

- **A. Longest sequence of a single character:**

```python
    string = "aabbccddddeee"
    max_char = string[0]
    max_count = 1
    current_char = string[0]
    current_count = 1
    for i in range(1, len(string)):
        if string[i] == current_char:
            current_count += 1
        else:
            current_char = string[i]
            current_count = 1
        if current_count > max_count:
            max_char = current_char
            max_count = current_count
    print(max_char * max_count)
```


- **B. Print all substrings of a string:**
```python
    string = "abc"
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    print(substrings)
```

- **C. Longest substring without repeating characters:**

```python
    string = "abcabcbb"
    longest = ""

    for i in range(len(string)):
        substring = ""
        is_unique = True
        for j in range(i, len(string)):
            if string[j] in substring:
                is_unique = False
            if is_unique:
                substring += string[j]
            else:
                # Once a non-unique character is found, stop adding to substring
                break
        if len(substring) > len(longest):
            longest = substring

    print(longest)

```

- **D. Find the first non-repeating character:**

```python
    string = "aabbccdde"
    non_repeating = ""
    found = False

    for i in range(len(string)):
        repeating = False
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                repeating = True
                # The inner loop will complete even if repeating is found
        if not repeating:
            non_repeating = string[i]
            found = True
            # If found is True, set a flag to stop processing further
            # But since we cannot use break, we handle it outside of this loop

    # After the loop ends, if we have found a non-repeating character, set it
    if found:
        print(non_repeating)
    else:
        print("No non-repeating character found")

```

- **E. Remove all non-alphabetic characters:**

```python
    string = "hello123world!"
    result = ""
    for char in string:
        if char.isalpha():
            result += char
    print(result)
```

### Exercise 7: Pattern Matching

- **7a. Check if a string matches a pattern of alternating characters:**

```python
    string = "ababab"
    alternating = True

    for i in range(2, len(string)):
        if string[i] != string[i % 2]:
            alternating = False
            # Instead of using break, use a flag to indicate that the string is not alternating
            # The loop will complete its iterations
            # We can then handle the result after the loop

    # After the loop ends, update alternating if needed
    # If `alternating` is False, it means we have detected non-alternating characters
    print(alternating)

```

- **B. Check if a string matches the pattern a*b*c*:**

```python
    string = "aaabbbccc"
    valid = True
    state = 0  # 0 for 'a', 1 for 'b', 2 for 'c'

    for char in string:
        if state == 0:
            if char == 'a':
                pass  # 'a' is valid in state 0
            elif char == 'b':
                state = 1
            else:
                valid = False
        elif state == 1:
            if char == 'b':
                pass  # 'b' is valid in state 1
            elif char == 'c':
                state = 2
            else:
                valid = False
        elif state == 2:
            if char == 'c':
                pass  # 'c' is valid in state 2
            else:
                valid = False

    # No need for further checks as loop completes naturally
    print(valid)

```

- **7c. Check if a string matches a specific format like "123-456-7890":**

```python
    string = "123-456-7890"
    valid = True

    # Check if the length is correct
    if len(string) != 12:
        valid = False
    else:
        for i in range(len(string)):
            if i in [3, 7]:
                # Check if hyphens are in the correct positions
                if string[i] != '-':
                    valid = False
            else:
                # Check if characters are digits
                if not string[i].isdigit():
                    valid = False

    # Output the result
    print(valid)

```

- **D. Check if a string has balanced parentheses:**

```python
    string = "(())()"
    balance = 0
    valid = True

    for char in string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1

        # Update valid based on the balance during the loop
        valid = valid and balance >= 0

    # Final check to ensure balance is zero
    valid = valid and balance == 0

    print(valid)
```

- **E. Check if a string contains only digits:**
  
```python
    string = "123456"
    is_digit = True

    for char in string:
        if '0' <= char <= '9':
            is_digit = is_digit and True
        else:
            is_digit = False

    print(is_digit)

```

### Exercise 8: Word-Level Operations

- **A. Count the number of words in a string:**

```python
    string = "Hello world"
    word_count = 1
    for char in string:
        if char == ' ':
            word_count += 1
    print(word_count)
```

- **B. Reverse the words in a string:**

```python
    string = "Hello world"
    words = []
    word = ""
    for char in string:
        if char == ' ':
            words.insert(0, word)
            word = ""
        else:
            word += char
    words.insert(0, word)
    reversed_words = " ".join(words)
    print(reversed_words)
```

- **8c. Find the longest word in a string:**
  
```python
    string = "Hello world from Python"
    longest_word = ""
    word = ""
    for char in string:
        if char == ' ':
            if len(word) > len(longest_word):
                longest_word = word
            word = ""
        else:
            word += char
    if len(word) > len(longest_word):
        longest_word = word
    print(longest_word)
```

- **D. Count occurrences of a word in a string:**

```python
    string = "hello world hello"
    word = "hello"
    words = []
    current_word = ""
    for char in string:
        if char == ' ':
            words.append(current_word)
            current_word = ""
        else:
            current_word += char
    words.append(current_word)
    word_count = 0
    for w in words:
        if w == word:
            word_count += 1
    print(word_count)
```

- **E. Print words longer than a given length:**

```python
    string = "Hello world from Python"
    length = 4
    long_words = []
    word = ""
    for char in string:
        if char == ' ':
            if len(word) > length:
                long_words.append(word)
            word = ""
        else:
            word += char
    if len(word) > length:
        long_words.append(word)
    print(long_words)
```

### Exercise 9: Custom Sorting

- **A. Sort a string alphabetically:**

```python
    string = "hello"
    sorted_string = ""
    for i in range(len(string)):
        smallest = string[i]
        for j in range(i + 1, len(string)):
            if string[j] < smallest:
                smallest = string[j]
        sorted_string += smallest
        string = string.replace(smallest, "", 1)
    print(sorted_string)
```

- **B. Sort words in a string by length:**

```python
    string = "Hello world from Python"
    words = []
    word = ""
    for char in string:
        if char == ' ':
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)
    sorted_words = []
    while words:
        shortest = words[0]
        for w in words:
            if len(w) < len(shortest):
                shortest = w
        sorted_words.append(shortest)
        words.remove(shortest)
    print(" ".join(sorted_words))
```

- **C. Sort a list of strings by their lengths:**

```python
    strings = ["Hello", "world", "from", "Python"]
    sorted_strings = []
    strings_copy = strings[:]  # Create a copy of the original list

    while strings_copy:
        # Find the shortest string
        shortest = strings_copy[0]
        for s in strings_copy:
            if len(s) < len(shortest):
                shortest = s

        # Build the sorted list using the + operator
        sorted_strings = sorted_strings + [shortest]

        # Create a new list excluding the shortest string
        # This avoids using break by iterating through the list
        new_strings_copy = []
        for s in strings_copy:
            if s != shortest:
                new_strings_copy = new_strings_copy + [s]
        
        strings_copy = new_strings_copy

    print(sorted_strings)

```

- **D. Sort characters in a string by their frequency:**
  
```python
    string = "hello"
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    sorted_chars = ""
    while frequency:
        max_char = max(frequency, key=frequency.get)
        sorted_chars += max_char * frequency[max_char]
        del frequency[max_char]
    print(sorted_chars)
```

- **E. Sort words in a string by their first letter:**
  
```python
    string = "Hello world from Python"
    words = []
    word = ""
    for char in string:
        if char == ' ':
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)
    sorted_words = []
    while words:
        first = words[0]
        for w in words:
            if w[0] < first[0]:
                first = w
        sorted_words.append(first)
        words.remove(first)
    print(" ".join(sorted_words))
```

### Exercise 10: Advanced String Operations
- **A. Check if two strings are anagrams:**

```python
string1 = "listen"
string2 = "silent"
sorted1 = ""
sorted2 = ""
for i in range(len(string1)):
    min_char = min(string1[i:])
    sorted1 += min_char
for i in range(len(string2)):
    min_char = min(string2[i:])
    sorted2 += min_char
print(sorted1 == sorted2)
```

- **B. Find the longest common prefix:**

```python
    strings = ["flower", "flow", "flight"]
    prefix = strings[0]

    for string in strings[1:]:
        temp_prefix = ""
        should_continue = True
        for i in range(len(prefix)):
            if should_continue and i < len(string) and prefix[i] == string[i]:
                temp_prefix += prefix[i]
            else:
                should_continue = False
        prefix = temp_prefix

    print(prefix)

```

- **C. Rotate a string by k positions:**

```python   
    string = "hello"
    k = 2
    rotated = string[k:] + string[:k]
    print(rotated)
```

- **D. Find the longest repeating substring:**

```python
string = "banana"
longest = ""
for i in range(len(string)):
    for j in range(i + 1, len(string)):
        substring = string[i:j]
        if substring in string[j:]:
            if len(substring) > len(longest):
                longest = substring
print(longest)

```

- **E. Merge two strings alternately:**

```python
 string1 = "abc"
    string2 = "xyz"
    merged = ""
    i, j = 0, 0
    while i < len(string1) or j < len(string2):
        if i < len(string1):
            merged += string1[i]
            i += 1
        if j < len(string2):
            merged += string2[j]
            j += 1
    print(merged)
```
