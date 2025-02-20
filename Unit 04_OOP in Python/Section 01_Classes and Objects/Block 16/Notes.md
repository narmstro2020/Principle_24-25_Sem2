# Python Object-Oriented Programming (OOP) Tutorial

## Table of Contents
1. Introduction to OOP
2. Classes and Objects
---

## 1. Introduction to OOP

### Vocabulary
| Term | Definition |
|------|------------|
| Object-Oriented Programming (OOP) | A programming paradigm based on objects and classes. |
| Class | A blueprint for creating objects. |
| Object | An instance of a class. |
| Method | A function defined inside a class that operates on instances. |
| Attribute | A variable that belongs to an object. |

### Description
Object-Oriented Programming (OOP) is a paradigm in which we model real-world entities using classes and objects. It allows for better organization, modularity, and code reuse.

### Example
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.display_info()
```

---

## 2. Classes and Objects

### Vocabulary
| Term | Definition |
|------|------------|
| Class | A template for creating objects. |
| Object | A specific instance of a class. |

### Description
A **class** is a blueprint, while an **object** is an instance of that class. Each object can have its own unique data.

### Example
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()
```

---

## 14. Examples

### Examples 1: Employee Management System
Create an `Employee` class with attributes like name, salary, and department. Add class methods to modify company policies.
```python
class Employee:
    company_policy = "Work from office"
    
    @classmethod
    def update_policy(cls, new_policy):
        cls.company_policy = new_policy
```
### Examples 2: Shape Hierarchy
Create a `Shape` base class and derive `Circle` and `Rectangle` classes with an area method.
```python
from math import pi

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2
```
---


