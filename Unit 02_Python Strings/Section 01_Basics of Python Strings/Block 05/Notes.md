
# Python Strings Tutorial

## Vocabulary

- **String**: A sequence of characters enclosed in quotes (single, double, or triple quotes).
- **Concatenation**: Joining two or more strings into one.
- **Slicing**: Extracting a part of a string.
- **Immutable**: Strings cannot be changed after they are created.
- **Escape Character**: A backslash (`\`) used to include special characters in strings.
- **String Literal**: A sequence of characters enclosed in quotes.
- **Method**: A function that operates on a string object.

---

## String Basics

### Creating Strings
Strings in Python are created by enclosing characters in quotes:

```python
# Single quotes
single_quote_string = 'Hello'

# Double quotes
double_quote_string = "World"

# Triple quotes (useful for multiline strings)
triple_quote_string = '''This is a multiline string.'''
```

### String Immutability
Strings are immutable, meaning you cannot modify them directly after creation:

```python
my_string = "Python"
# This will raise an error
my_string[0] = 'J'
```

### Escape Characters
Escape characters allow inclusion of special characters:

| Escape Sequence | Meaning          |
|-----------------|------------------|
| `\n`           | Newline          |
| `\t`           | Tab              |
| `\\`          | Backslash        |
| `\"`          | Double quote     |
| `\'`          | Single quote     |

Example:
```python
print("Hello\nWorld")
```
Output:
```
Hello
World
```

---

## String Operations

### Concatenation
Strings can be joined using the `+` operator:

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World
```

### Repetition
The `*` operator repeats a string:

```python
print("Hello" * 3)  # Output: HelloHelloHello
```

### Membership Testing
Use `in` to check if a substring exists:

```python
print("Py" in "Python")  # Output: True
```

---

## String Methods

### Commonly Used Methods

1. **`len()`**: Returns the length of a string.
   ```python
   print(len("Python"))  # Output: 6
   ```

2. **`lower()` and `upper()`**: Converts case.
   ```python
   print("Python".lower())  # Output: python
   print("Python".upper())  # Output: PYTHON
   ```

3. **`strip()`**: Removes leading and trailing spaces.
   ```python
   print("  Python  ".strip())  # Output: Python
   ```

4. **`replace()`**: Replaces parts of a string.
   ```python
   print("Hello World".replace("World", "Python"))  # Output: Hello Python
   ```

5. **`split()`**: Splits a string into a list.
   ```python
   print("Hello,World".split(","))  # Output: ['Hello', 'World']
   ```

6. **`join()`**: Joins elements of a list into a string.
   ```python
   words = ["Hello", "World"]
   print(" ".join(words))  # Output: Hello World
   ```

---

## Slicing Strings

Strings can be sliced using the `start:end:step` syntax:

```python
string = "Python"
print(string[0:3])    # Output: Pyt
print(string[:3])     # Output: Pyt
print(string[3:])     # Output: hon
print(string[::-1])   # Output: nohtyP
```

---