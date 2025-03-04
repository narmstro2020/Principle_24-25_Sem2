# Assignment 1
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        #TODO: make a self.radius and assign radius to it.
        ... #TODO: remove this .. when done

    def area(self):
        #TODO: return the area of a circle using self.radius
        #TODO (cont.): the area of a circle is pi * (radius ** 2)
        #TODO (cont.): again don't forget self.
        ... #TODO: remove this .. when done

#TODO: you do the Rectangle in the same way we did a circle.  Except
#(cont.) instead of a radius you'll need width and length for the init method
#(cont.) and the area will width * length.  Again don't forget self.

#TODO: make a circle and print out its area by calling it.
#TODO: do the same for a rectangle

# Assignment 2

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        #TODO: return an f string that print out the balance of the account
        #TODO: (cont.) format of the string: "{owner}'s Account: Balance of {balance}
        ... #TODO: remove this .. when done

    def __add__(self, other):
        #TODO: return the sum of self.balance and other.balance
        ... #TODO: remove this .. when done

fred = BankAccount(500, "Fred")
ethel = BankAccount(600, "Ethel")
print(fred + ethel)
