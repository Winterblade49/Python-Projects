from abc import ABC, abstractmethod

# Parent class with an abstract method
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def regular_method(self):
        print("This is a regular method.")

# Child class that extends the parent class
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method.")

# Creating an object of the child class
obj = ConcreteClass()

# Calling the abstract method (implemented in the child class)
obj.abstract_method()

# Calling the regular method (inherited from the parent class)
obj.regular_method()
