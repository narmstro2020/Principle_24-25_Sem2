
# Python OOP: Instance Variables, Class Variables, Instance Methods, Class Methods, and Static Methods

## Vocabulary

| Term              | Definition                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------|
| Instance Variable | A variable that is defined inside a class and belongs to an object (instance) of the class.   |
| Class Variable    | A variable shared by all instances of a class. Defined within the class but outside methods.  |
| Instance Method   | A method that operates on an instance of the class. It has access to instance variables.      |
| Class Method      | A method bound to the class, not the instance. It modifies class variables and uses @classmethod. |
| Static Method     | A method that doesn’t operate on an instance or class variables. Uses @staticmethod decorator. |
| Self              | A reference to the current instance of the class.                                             |
| cls               | A reference to the class itself, used inside class methods.                                   |

---

## 1. Instance Variables and Methods

### Detailed Description
Instance variables are unique to each instance of a class. They are defined within the `__init__` method and can have different values for different objects. Instance methods operate on instance variables and require the `self` parameter.

### Example Code
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    def display_info(self):  # Instance method
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing instance methods
car1.display_info()  # Output: Brand: Toyota, Model: Corolla
car2.display_info()  # Output: Brand: Honda, Model: Civic
```

### Key Points
- Each instance has its own copy of instance variables.
- Instance methods can access and modify instance variables.

---

## 2. Class Variables and Class Methods

### Detailed Description
Class variables are shared across all instances of a class. They are defined directly within the class but outside any instance methods. Class methods operate on these variables and are marked using the `@classmethod` decorator. They take `cls` as the first parameter instead of `self`.

### Example Code
```python
class Employee:
    company_name = "TechCorp"  # Class variable
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def display_company_info(cls):  # Class method
        print(f"Company: {cls.company_name}, Total Employees: {cls.employee_count}")

# Creating instances
emp1 = Employee("Alice")
emp2 = Employee("Bob")

# Accessing class method
Employee.display_company_info()  # Output: Company: TechCorp, Total Employees: 2
```

### Key Points
- Shared across all instances.
- Can be accessed using both `cls.variable` and `self.variable`.
- Class methods can modify class variables.

---

## 3. Static Methods

### Detailed Description
Static methods do not modify class or instance variables. They are defined using the `@staticmethod` decorator and are utility functions within the class context.

### Example Code
```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Accessing static methods
result1 = Calculator.add(5, 3)
result2 = Calculator.subtract(10, 4)

print(f"Addition Result: {result1}")  # Output: Addition Result: 8
print(f"Subtraction Result: {result2}")  # Output: Subtraction Result: 6
```

### Key Points
- Doesn’t require `self` or `cls`.
- Useful for utility or helper methods within a class.

---

## Examples

### Example 1: Geometry Utilities
Create a `Geometry` class with:
- Static method: `calculate_area_circle(radius)`.
- Static method: `calculate_area_rectangle(length, width)`.
- Static method: `calculate_area_square(side)`.
```python
class Geometry:
    @staticmethod
    def calculate_area_circle(radius):
        return 3.14 * radius ** 2

    @staticmethod
    def calculate_area_rectangle(length, width):
        return length * width

    @staticmethod
    def calculate_area_square(side):
        return side ** 2
```
---
