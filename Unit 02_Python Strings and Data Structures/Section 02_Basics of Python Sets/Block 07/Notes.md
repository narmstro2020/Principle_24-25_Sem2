
# Tutorial on Sets in Python

## Table of Contents
1. Introduction to Sets
2. Key Vocabulary
3. Properties of Sets
4. Creating Sets
5. Accessing and Iterating Through Sets
6. Modifying Sets
7. Set Operations
   - Union
   - Intersection
   - Difference
   - Symmetric Difference
8. Built-in Methods for Sets
9. Use Cases of Sets
10. Assignments
11. Assignment Solutions

---

## 1. Introduction to Sets
Sets are one of the built-in data types in Python used to store collections of unique elements. Unlike lists and tuples, sets do not allow duplicate elements, and their items are unordered.

### Example:
```python
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}
```

---

## 2. Key Vocabulary
- **Set**: A collection of unique and unordered elements.
- **Immutable**: Elements within a set must be immutable (e.g., numbers, strings, tuples).
- **Mutable**: The set itself can be modified, e.g., elements can be added or removed.
- **Union**: Combines all elements from two sets.
- **Intersection**: Retains only elements common to both sets.
- **Difference**: Returns elements present in one set but not the other.
- **Symmetric Difference**: Returns elements present in either of the sets but not in both.

---

## 3. Properties of Sets
1. **Unordered**: Elements do not have a specific order.
2. **Unique**: Duplicate elements are automatically removed.
3. **Mutable**: You can add or remove elements from a set.
4. **Heterogeneous**: Sets can hold a mix of data types.

### Example:
```python
my_set = {1, "Python", (3, 4)}
print(my_set)  # Output: {1, 'Python', (3, 4)}
```

---

## 4. Creating Sets

### Empty Set:
```python
empty_set = set()  # Use the set() function
```

### Non-Empty Set:
```python
fruits = {"apple", "banana", "cherry"}
```

### From Other Iterables:
```python
numbers = set([1, 2, 3, 3, 4])  # Duplicates are removed
print(numbers)  # Output: {1, 2, 3, 4}
```

---

## 5. Accessing and Iterating Through Sets

### Accessing:
Elements in a set cannot be accessed using an index as sets are unordered.

### Iterating:
```python
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)
```

---

## 6. Modifying Sets

### Adding Elements:
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

### Removing Elements:
```python
my_set.remove(3)  # Raises KeyError if element not found
my_set.discard(5)  # Does not raise an error if element not found
```

### Clearing All Elements:
```python
my_set.clear()
print(my_set)  # Output: set()
```

---

## 7. Set Operations

### Union:
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

### Intersection:
```python
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {3}
```

### Difference:
```python
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```

### Symmetric Difference:
```python
sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}
```

---

## 8. Built-in Methods for Sets

- `add()`: Adds an element to the set.
- `remove()`: Removes an element, raises KeyError if not found.
- `discard()`: Removes an element, does not raise an error if not found.
- `pop()`: Removes and returns a random element.
- `clear()`: Removes all elements from the set.
- `copy()`: Returns a shallow copy of the set.

---

## 9. Use Cases of Sets
1. Removing duplicates from a list.
2. Membership testing (e.g., checking if an element exists).
3. Performing mathematical operations like union and intersection.
4. Storing items that need to remain unique.

---

This tutorial provides a comprehensive guide to understanding and using sets in Python. By completing the assignments, you will gain practical experience working with this versatile data structure.
