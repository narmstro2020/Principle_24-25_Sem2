# Python Advanced OOP Concepts

## Table of Contents
1. **Abstract Classes**
2. **Interfaces in Python**
3. **Special Methods (Dunder Methods)**
4. **Multiple Inheritance**
5. **Composition vs. Inheritance**
6. **Property Decorators**
7. **Assignments**
8. **Solutions**

---

## 1. Abstract Classes

### Vocabulary
| Term | Definition |
|------|------------|
| Abstract Class | A class that cannot be instantiated and is meant to be subclassed. |
| Abstract Method | A method declared in an abstract class that must be implemented in subclasses. |
| `ABC` (Abstract Base Class) | A module in Python (`abc`) that allows defining abstract classes. |

### Description
Abstract classes are used to define common interfaces for a set of related classes. They ensure that subclasses implement certain methods while preventing instantiation of the abstract class itself.

Python provides the `abc` module for creating abstract classes.

### Example Code
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# dog = Animal()  # This will raise an error

d = Dog()
print(d.make_sound())  # Output: Bark!
```

---

## 2. Interfaces in Python

### Vocabulary
| Term | Definition |
|------|------------|
| Interface | A contract specifying methods that a class must implement. |
| Protocol (Python 3.8+) | A way to define structural subtyping using `typing.Protocol`. |

### Description
Python does not have explicit interfaces like Java or C#. Instead, it uses abstract base classes (ABCs) or typing protocols to enforce method implementation.

### Example Code
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car is moving"

c = Car()
print(c.move())  # Output: Car is moving
```

Using `Protocol`:
```python
from typing import Protocol

class Movable(Protocol):
    def move(self) -> str:
        ...

class Bike:
    def move(self):
        return "Bike is moving"

b = Bike()
print(b.move())
```

---

## 3. Special Methods (Dunder Methods)

### Vocabulary
| Term | Definition |
|------|------------|
| Dunder Method | A method with double underscores (e.g., `__init__`, `__str__`). |
| Magic Method | Another name for dunder methods. |

### Description
Dunder methods allow customization of built-in behavior of objects, such as object creation, string representation, iteration, etc.

### Example Code
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __add__(self, other):
        return self.age + other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(str(p1))  # Output: Person(name=Alice, age=25)
print(p1 + p2)  # Output: 55
```

---

## 4. Multiple Inheritance

### Vocabulary
| Term | Definition |
|------|------------|
| Multiple Inheritance | A feature allowing a class to inherit from more than one parent class. |
| MRO (Method Resolution Order) | The order in which methods are looked up in the inheritance hierarchy. |

### Example Code
```python
class A:
    def say_hello(self):
        return "Hello from A"

class B:
    def say_hello(self):
        return "Hello from B"

class C(A, B):
    pass

c = C()
print(c.say_hello())  # Output: Hello from A (follows MRO)
```

---

## 5. Composition vs. Inheritance

### Vocabulary
| Term | Definition |
|------|------------|
| Composition | Creating complex objects by combining simpler objects. |
| Inheritance | Creating a hierarchy of classes where child classes extend functionality. |

### Example Code
#### Inheritance
```python
class Engine:
    def start(self):
        return "Engine started"

class Car(Engine):
    pass

c = Car()
print(c.start())  # Output: Engine started
```

#### Composition
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

c = Car()
print(c.start())  # Output: Engine started
```

---

## 6. Property Decorators

### Vocabulary
| Term | Definition |
|------|------------|
| Property Decorator | A method decorator that makes a method behave like an attribute. |

### Example Code
```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

p = Product(50)
print(p.price)  # Output: 50
p.price = 60  # Works fine
```

---

## 7. Examples

### Multiple Inheritance
Create two classes `Flyable` and `Swimmable`, then create a class `Duck` that inherits from both and implements their behaviors.
```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass

d = Duck()
print(d.fly())  # Output: Flying
```
---



