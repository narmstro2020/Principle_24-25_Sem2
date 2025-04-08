
# 📘 Python Tutorial: Files and Modules

## 📂 Table of Contents

1. Introduction to Files  
2. Opening and Closing Files  
3. Reading from Files  
4. Writing to Files  
5. Working with `with` Statement  
6. File Modes  
7. File Paths (Absolute vs. Relative)  
8. Working with Directories using `os` and `pathlib`  
9. Handling File Exceptions  
10. Introduction to Modules  
11. Importing Modules  
12. Creating Custom Modules  
13. Using `__name__ == "__main__"` Idiom  
14. Assignment 1 – File Analyzer  
15. Assignment 2 – To-Do List App with File Storage  
16. Assignment 3 – Modular Calculator  
17. Summary and Best Practices

---

## 1. 📘 Introduction to Files

Files are a way to store data permanently. Python can read from and write to many types of files, including `.txt`, `.csv`, `.json`, etc.

---

## 2. 📂 Opening and Closing Files

```python
file = open("folder/example.txt", "r")  # open file in read mode
print(file.read())
file.close()
```

---

## 3. 📖 Reading from Files

```python
# Read all content
content = file.read()

# Read line by line
for line in file:
    print(line.strip())

# Read single line
line = file.readline()
```

---

## 4. 🖊️ Writing to Files

```python
file = open("output.txt", "w")
file.write("Hello, world!\n")
file.close()
```

---

## 5. ✅ Working with `with` Statement

Automatically closes file:

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

## 6. 🔧 File Modes

| Mode | Meaning              |
|------|----------------------|
| `r`  | Read                 |
| `w`  | Write (overwrite)    |
| `a`  | Append               |
| `r+` | Read and write       |
| `b`  | Binary mode          |

---

## 7. 📁 File Paths

```python
# Absolute path
file = open("/Users/you/Documents/file.txt")

# Relative path
file = open("folder/file.txt")
```

---

## 8. 🛠️ Working with Directories

```python
import os

print(os.getcwd())  # current directory
os.listdir()        # list files
os.mkdir("new_folder")  # create folder

from pathlib import Path

path = Path("data/file.txt")
print(path.exists())
```

---

## 9. 🚫 Handling File Exceptions

```python
try:
    with open("missing.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

---

## 10. 📦 Introduction to Modules

A **module** is any `.py` file containing Python code (functions, classes, variables).

---

## 11. 📥 Importing Modules

```python
import math
from math import sqrt

print(math.pi)
print(sqrt(16))
```

---

## 12. ✍️ Creating Custom Modules

**math_utils.py**
```python
def add(x, y):
    return x + y
```

**main.py**
```python
import math_utils

print(math_utils.add(3, 4))
```

---

## 13. 🚀 The `__name__ == "__main__"` Idiom

```python
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()  # Only runs if this file is the main script
```




---

## 🧠 Summary and Best Practices

- Always use `with open(...)` for file operations.
- Use `os` or `pathlib` for path manipulation.
- Create reusable modules for better structure.
- Use `__name__ == "__main__"` to separate script from importable logic.
- Handle file exceptions to make programs robust.
