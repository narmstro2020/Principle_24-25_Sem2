# Python Dictionaries Tutorial

## Introduction to Python Dictionaries

### Vocabulary
1. **Dictionary**: A collection of key-value pairs.
2. **Key**: An immutable and unique identifier in a dictionary.
3. **Value**: Data associated with a key in a dictionary.
4. **Key-Value Pair**: A combination of a key and its associated value.
5. **Hashable**: An object is hashable if it has a hash value that does not change during its lifetime.
6. **Mutable**: Capable of being changed after creation.

### What is a Dictionary?
A dictionary in Python is a mutable, unordered collection of key-value pairs. Each key is unique and serves as an identifier for its associated value. Dictionaries are optimized for quick lookups and are implemented as hash tables under the hood.

```python
# Example of a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

## Key Features of Dictionaries
1. **Unordered**: Items in a dictionary are not stored in any particular order.
2. **Mutable**: You can modify, add, or delete key-value pairs after the dictionary is created.
3. **Keys are unique**: No duplicate keys are allowed.
4. **Keys are hashable**: Only immutable data types like strings, numbers, or tuples can be used as keys.

## Creating Dictionaries
### Using Curly Braces
```python
# Example
my_dict = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2021
}
```

### Using the `dict()` Constructor
```python
# Example
my_dict = dict(brand="Toyota", model="Corolla", year=2021)
```

## Accessing Data in Dictionaries
### Accessing Values by Key
```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])  # Output: Alice
```

### Using the `get()` Method
```python
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("gender", "Not specified"))  # Output: Not specified
```

## Modifying Dictionaries
### Adding or Updating Key-Value Pairs
```python
my_dict["city"] = "New York"  # Adds a new key-value pair
my_dict["age"] = 31  # Updates an existing value
```

### Removing Key-Value Pairs
- Using `del`:
  ```python
  del my_dict["city"]
  ```
- Using `pop()`:
  ```python
  age = my_dict.pop("age")  # Removes the key and returns its value
  ```
- Using `popitem()`:
  ```python
  last_item = my_dict.popitem()  # Removes and returns the last inserted key-value pair
  ```

## Looping Through Dictionaries
### Looping Through Keys
```python
for key in my_dict:
    print(key)
```

### Looping Through Values
```python
for value in my_dict.values():
    print(value)
```

### Looping Through Key-Value Pairs
```python
for key, value in my_dict.items():
    print(key, value)
```

## Dictionary Methods
| Method       | Description                                       |
|--------------|---------------------------------------------------|
| `clear()`    | Removes all key-value pairs.                     |
| `copy()`     | Returns a shallow copy of the dictionary.        |
| `fromkeys()` | Creates a new dictionary with specified keys.    |
| `items()`    | Returns a view object of key-value pairs.        |
| `keys()`     | Returns a view object of keys.                  |
| `values()`   | Returns a view object of values.                |
| `update()`   | Updates the dictionary with another dictionary. |


## Conclusion
Python dictionaries are powerful and versatile tools for managing data in key-value pairs. With their rich set of methods and flexibility, dictionaries are an essential part of Python programming. Practice with the assignments above to gain a deeper understanding of how to use them effectively.