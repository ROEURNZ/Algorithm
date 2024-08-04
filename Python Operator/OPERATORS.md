# Python Operators Reference

## Overview

This document provides a comprehensive reference for all the operators available in Python, categorized by their function.

## Table of Contents

- [Arithmetic Operators](#arithmetic-operators)
- [Comparison Operators](#comparison-operators)
- [Logical Operators](#logical-operators)
- [Assignment Operators](#assignment-operators)
- [Bitwise Operators](#bitwise-operators)
- [Membership Operators](#membership-operators)
- [Identity Operators](#identity-operators)

## 1. Arithmetic Operators

Used for mathematical operations.

| Operator | Name           | Example    |
| -------- | -------------- | ---------- |
| `+`    | Addition       | `a + b`  |
| `-`    | Subtraction    | `a - b`  |
| `*`    | Multiplication | `a * b`  |
| `/`    | Division       | `a / b`  |
| `%`    | Modulus        | `a % b`  |
| `**`   | Exponentiation | `a ** b` |
| `//`   | Floor Division | `a // b` |

### Examples

```python
a = 10
b = 5

print(a + b)  # 15
print(a - b)  # 5
print(a * b)  # 50
print(a / b)  # 2.0
print(a % b)  # 0
print(a ** b) # 100000
print(a // b) # 2
```


## 2. Comparison Operators

Used to compare two values.

| Operator | Name                     | Example    |
| -------- | ------------------------ | ---------- |
| `==`   | Equal                    | `a == b` |
| `!=`   | Not equal                | `a != b` |
| `>`    | Greater than             | `a > b`  |
| `<`    | Less than                | `a < b`  |
| `>=`   | Greater than or equal to | `a >= b` |
| `<=`   | Less than or equal to    | `a <= b` |

### Examples

```python
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
```


## 3. Assignment Operators

Used to assign values to variables.

| Operator | Name                      | Example     |
| -------- | ------------------------- | ----------- |
| `=`    | Assign                    | `a = b`   |
| `+=`   | Add and assign            | `a += b`  |
| `-=`   | Subtract and assign       | `a -= b`  |
| `*=`   | Multiply and assign       | `a *= b`  |
| `/=`   | Divide and assign         | `a /= b`  |
| `%=`   | Modulus and assign        | `a %= b`  |
| `**=`  | Exponent and assign       | `a **= b` |
| `//=`  | Floor division and assign | `a //= b` |

### Examples

```python
a = 5
a += 3  # a = a + 3
print(a) # 8
```



## 4. Logical Operators

Used to combine conditional statements.

| Operator | Name        | Example     |
| -------- | ----------- | ----------- |
| `and`  | Logical AND | `a and b` |
| `or`   | Logical OR  | `a or b`  |
| `not`  | Logical NOT | `not a`   |

### Examples

```python
a = True
b = False

print(a and b) # False
print(a or b)  # True
print(not a)   # False
```



## 5. Bitwise Operators

Used for bit-level operations.

| Operator | Name                | Example    |
| -------- | ------------------- | ---------- |
| `&`    | Bitwise AND         | `a & b`  |
| `        | `                   | Bitwise OR |
| `^`    | Bitwise XOR         | `a ^ b`  |
| `~`    | Bitwise NOT         | `~a`     |
| `<<`   | Bitwise left shift  | `a << b` |
| `>>`   | Bitwise right shift | `a >> b` |

### Examples

```python
x = 6  # 110 in binary
y = 3  # 011 in binary

print(x & y)  # 2 (010 in binary)
print(x | y)  # 7 (111 in binary)
print(x ^ y)  # 5 (101 in binary)
print(~x)     # -7 (inverting all bits)
print(x << 1) # 12 (1100 in binary)
print(x >> 1) # 3 (011 in binary)
```



## 6. Membership Operators

Used to test if a sequence contains a value.

| Operator   | Name   | Example        |
| ---------- | ------ | -------------- |
| `in`     | In     | `x in y`     |
| `not in` | Not in | `x not in y` |

### Examples

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)    # True
print("grape" not in fruits) # True
```



## 7. Identity Operators

Used to compare objects' identities.

| Operator   | Name   | Example        |
| ---------- | ------ | -------------- |
| `is`     | Is     | `a is b`     |
| `is not` | Is not | `a is not b` |

### Examples

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      # True
print(x is y)      # False
print(x == y)      # True (because x and y have the same content)
print(x is not y)  # True
```
