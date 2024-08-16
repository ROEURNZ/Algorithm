
# Python Data Types Reference

## Overview

Python provides a variety of built-in data types to handle different kinds of data. This document outlines the main data types and their subtypes, including numbers, sequences, booleans, sets, and dictionaries.

## Table of Contents

- [Numbers](#numbers)
  - [Integer](#integer-int)
  - [Floating Point](#floating-point-float)
  - [Complex](#complex-complex)
- [Sequence Types](#sequence-types)
  - [String](#string-str)
  - [List](#list-list)
  - [Tuple](#tuple-tuple)
- [Boolean](#boolean)
- [Set](#set)
- [Dictionary](#dictionary)

## Numbers

Python's numeric types represent different kinds of numerical values.

### Integer (`int`)

Represents whole numbers, both positive and negative.

| Example    |
| ---------- |
| `a = 10` |
| `b = -5` |

#### Subtypes

- **Short Integer**: Small integers stored in a fixed-size representation.
- **Long Integer**: Large integers that may require more space.

### Floating Point (`float`)

Represents real numbers with decimal points.

| Example       |
| ------------- |
| `a = 10.5`  |
| `b = -3.14` |

#### Subtypes

- **Single Precision**: Floats with limited precision (typically 32-bit).
- **Double Precision**: Floats with higher precision (typically 64-bit).

### Complex (`complex`)

Represents complex numbers with a real and imaginary part.

| Example         |
| --------------- |
| `a = 1 + 2j`  |
| `b = -3 + 4j` |

#### Subtypes

- **Standard Complex**: The standard representation using real and imaginary parts.

#### Examples

```python
# Integer
a = 10
b = -5

# Float
x = 10.5
y = -3.14

# Complex
z = 1 + 2j
w = -3 + 4j
```
