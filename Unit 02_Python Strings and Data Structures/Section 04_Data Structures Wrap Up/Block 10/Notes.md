# Python Data Structures and Collections Tutorial

## 1. Introduction
### What are Data Structures?
Data structures are ways of organizing and storing data to enable efficient access and modification. Python provides several built-in data structures, which are optimized for different use cases.

### Importance of Choosing the Right Data Structure
Using the right data structure can significantly affect the efficiency and performance of an application. Each data structure has unique characteristics, strengths, and weaknesses.

### Built-in vs. Custom Data Structures
Python provides built-in data structures such as lists, tuples, sets, and dictionaries. For advanced use cases, developers may implement custom data structures such as linked lists, trees, and graphs.

### Overview of Python’s Built-in Data Structures
- **Lists**: Ordered, mutable collections of items.
- **Tuples**: Ordered, immutable collections of items.
- **Sets**: Unordered collections of unique items.
- **Dictionaries**: Key-value mappings.

## 2. Standard Built-in Non-Collection Data Types
### 2.1 Integers
#### Definition and Properties
Integers are whole numbers without a fractional component.

#### Creating Integers
```python
num = 10
```

#### Operations
```python
sum_val = num + 5
product = num * 2
```

### 2.2 Floating-Point Numbers
#### Definition and Properties
Floating-point numbers represent real numbers with decimal points.

#### Creating Floats
```python
pi = 3.14
```

#### Operations
```python
result = pi * 2
```

### 2.3 Booleans
#### Definition and Properties
Booleans represent truth values: `True` or `False`.

#### Creating Booleans
```python
flag = True
```

#### Operations
```python
negation = not flag
```

### 2.4 Strings
#### Definition and Properties
Strings are sequences of characters.

#### Creating Strings
```python
text = "Hello, World!"
```

#### Operations
```python
uppercase = text.upper()
substring = text[0:5]
```

### 2.5 NoneType
#### Definition and Properties
NoneType represents the absence of a value and is commonly used for default function return values.

#### Creating NoneType
```python
value = None
```

#### Operations
```python
if value is None:
    print("Value is not set")
```

### 2.6 Complex Numbers
#### Definition and Properties
Complex numbers consist of a real and an imaginary part.

#### Creating Complex Numbers
```python
complex_num = 2 + 3j
```

#### Operations
```python
real_part = complex_num.real
imaginary_part = complex_num.imag
conjugate = complex_num.conjugate()
```

## 3. Built-in Data Structures

### 3.1 Lists
#### Definition and Properties
A list is an ordered, mutable collection of items. Lists allow duplicate elements and can store multiple data types.

#### Creating Lists
```python
my_list = [1, 2, 3, "hello", True]
```

#### Accessing Elements
```python
print(my_list[0])  # First element
print(my_list[-1]) # Last element
```

#### List Operations
```python
my_list.append(4)  # Add element to the end
my_list.insert(1, "new")  # Insert at index
my_list.remove(2)  # Remove element
my_list.pop()  # Remove and return the last element
```

#### List Comprehensions
```python
squared = [x**2 for x in range(10)]
```

#### Nested Lists
```python
nested = [[1, 2, 3], [4, 5, 6]]
```

#### Performance Considerations
Lists have O(1) time complexity for appending but O(n) for searching.

### 3.2 Tuples
#### Definition and Properties
A tuple is an ordered, immutable collection of items.

#### Creating Tuples
```python
my_tuple = (1, 2, 3, "hello")
```

#### Accessing Elements
```python
print(my_tuple[1])
```

#### Tuple Operations
```python
new_tuple = my_tuple + (4, 5)
```

### 3.3 Sets
#### Definition and Properties
A set is an unordered collection of unique elements.

#### Creating Sets
```python
my_set = {1, 2, 3, 4}
```

#### Set Operations
```python
my_set.add(5)
my_set.remove(3)
union_set = my_set | {6, 7}
```

### 3.4 Dictionaries
#### Definition and Properties
A dictionary is a key-value mapping.

#### Creating Dictionaries
```python
my_dict = {"name": "Alice", "age": 25}
```

#### Accessing Elements
```python
print(my_dict["name"])
```

#### Dictionary Operations
```python
my_dict["city"] = "New York"
```

## 4. Advanced Data Structures in Python

### 4.1 Stacks
#### Definition
A stack follows the LIFO (Last-In-First-Out) principle.

#### Implementing Stacks
```python
stack = []
stack.append(1)
stack.pop()
```

### 4.2 Queues
#### Definition
A queue follows the FIFO (First-In-First-Out) principle.

#### Implementing Queues
```python
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()
```

### 4.3 Linked Lists
#### Definition
A linked list consists of nodes, where each node contains a value and a reference to the next node.

#### Implementing a Singly Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

This tutorial provides a structured and comprehensive guide to Python data structures. Let me know if you need additional details or modifications!
