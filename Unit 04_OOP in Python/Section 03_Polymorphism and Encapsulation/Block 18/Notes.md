# Python Object-Oriented Programming: Encapsulation, Inheritance, and Polymorphism

## Introduction
Object-Oriented Programming (OOP) in Python is a paradigm that helps structure code using objects and classes. Three key principles of OOP are **Encapsulation, Inheritance, and Polymorphism**. This tutorial covers these concepts in detail.

---

## 1. Encapsulation
### Vocabulary
| Term          | Definition |
|--------------|------------|
| Encapsulation | The process of restricting access to certain details of an object and only exposing necessary functionalities. |
| Private Attribute | An attribute prefixed with `__` (double underscore) to prevent direct access outside the class. |
| Getter Method | A method used to retrieve the value of a private attribute. |
| Setter Method | A method used to update the value of a private attribute with validation. |

### Detailed Description
Encapsulation ensures that an object's internal representation is hidden from the outside. This prevents unintended modifications and promotes **data security**.

### Example Code
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Example usage
account = BankAccount("Alice", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)  # Output: Invalid withdrawal amount or insufficient balance.
```

---

## 2. Inheritance
### Vocabulary
| Term          | Definition |
|--------------|------------|
| Inheritance  | A mechanism that allows a class to inherit attributes and methods from another class. |
| Parent Class | The class whose attributes and methods are inherited. |
| Child Class  | The class that inherits from another class. |
| Method Overriding | When a child class redefines a method from the parent class. |

### Detailed Description
Inheritance allows **code reusability** by enabling a new class (child) to inherit attributes and methods from an existing class (parent).

### Example Code
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):  # Method overriding
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name, "says", dog.make_sound())  # Output: Buddy says Bark
print(cat.name, "says", cat.make_sound())  # Output: Whiskers says Meow
```

---

## 3. Polymorphism
### Vocabulary
| Term          | Definition |
|--------------|------------|
| Polymorphism | The ability of different classes to be treated as instances of the same class through a shared interface. |
| Method Overriding | When a child class provides a specific implementation for a method already defined in its parent class. |
| Duck Typing  | A Python-specific feature where an object's behavior is determined by its methods and attributes rather than its type. |

### Detailed Description
Polymorphism allows different object types to be used interchangeably as long as they share a common interface (methods with the same name).

### Example Code
```python
class Bird:
    def make_sound(self):
        return "Chirp"

class Dog:
    def make_sound(self):
        return "Bark"

class Cat:
    def make_sound(self):
        return "Meow"

# Function that uses polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Example usage
animals = [Bird(), Dog(), Cat()]
for animal in animals:
    animal_sound(animal)
```

---

## Examples


### Example 1: Inheritance
- Create a `Person` class with attributes `name` and `age`.
- Create two subclasses: `Student` (with `grade`) and `Teacher` (with `subject`).
- Implement a method `describe()` in each class to print details.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describe(self):
        return f"{self.name} is {self.age} years old."

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def describe(self):
        return f"{self.name} is a student in grade {self.grade}."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def describe(self):
        return f"{self.name} teaches {self.subject}."
```
### Example 2: Polymorphism
- Create a parent class `Shape` with a method `area()`.
- Create subclasses `Rectangle` (attributes: width, height) and `Circle` (attribute: radius).
- Implement the `area()` method in each subclass to compute the area.
- Write a function that takes a `Shape` object and prints its area.
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

def print_area(shape):
    print("Area:", shape.area())
```
---
