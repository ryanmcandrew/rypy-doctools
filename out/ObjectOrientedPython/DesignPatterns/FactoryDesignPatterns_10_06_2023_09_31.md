
factory design patterns
=======================
Introduction:

Python is a high-level programming language that is known for its simplicity, readability, and ease of use. Design patterns are a proven way to design robust, reusable, and scalable software. A design pattern is a solution to a commonly occurring problem in software design. The Factory design pattern is one of the most widely used design patterns that helps to create objects without exposing the creation logic to the client.

This article will guide you through Factory Design Patterns in Python 3.10. You will learn what design patterns are and why they are important. Additionally, you will learn how to implement the Factory Design Pattern step-by-step in Python.

Prerequisites:

Before we dive into the implementation of the Factory Design Pattern in Python, you need to have the following:

- Basic knowledge of Python programming language
- Basic understanding of object-oriented programming concepts

Steps to Implement Factory Design Pattern:

The implementation of the Factory Design Pattern in Python involves the following steps:

Step 1: Identify the problem you want to solve

The Factory Design Pattern is used when we want to create objects without exposing the creation logic to the client. This pattern is useful when the creation process is complex or when there are multiple ways to create an object.

For example, suppose we have a software that allows users to create different types of animals, such as dogs, cats, and elephants. We want to provide an interface for the users to create these animals, but we don't want to expose the creation logic to the client.

In this case, we can use the Factory Design Pattern to create animal objects without exposing the creation logic to the client.

Step 2: Define the product interface

The product interface defines the methods that all products that the factory creates must implement. In our example, all animals (products) that the factory creates should have the following methods:

- Sound - returns the sound that the animal makes.
- Action - returns the action that the animal does.

The product interface is as follows:

```python
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def action(self):
        pass
```

Step 3: Create concrete products

A concrete product is a class that implements the product interface. In our example, we have three concrete product classes:

- Dog
- Cat
- Elephant

The concrete product classes look like this:

```python
class Dog(Animal):
    
    def sound(self):
        return "Woof"
    
    def action(self):
        return "Run"
    
    
class Cat(Animal):
    
    def sound(self):
        return "Meow"
    
    def action(self):
        return "Jump"
    
    
class Elephant(Animal):
    
    def sound(self):
        return "Trumpet"
    
    def action(self):
        return "Walk"
```

Step 4: Define the factory interface

The factory interface defines the methods that the factory should implement. In our example, we have only one method - create_animal(). This method creates and returns an instance of the concrete product class.

The factory interface looks like this:

```python
from abc import ABCMeta, abstractmethod

class AnimalFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def create_animal(self, animal_type: str) -> Animal:
        pass
```

Step 5: Create concrete factories

A concrete factory is a class that implements the factory interface. In our example, we have one concrete factory class - AnimalFactoryImpl. This class creates and returns an instance of the concrete product class based on the animal type passed as an argument.

The concrete factory implementation looks like this:

```python
class AnimalFactoryImpl(AnimalFactory):
    
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == 'Dog':
            return Dog()
        elif animal_type == 'Cat':
            return Cat()
        elif animal_type == 'Elephant':
            return Elephant()
        else:
            return None
```

Step 6: Test the implementation

To test the factory implementation, we can create an instance of the concrete factory class and use its create_animal() method to create animal objects.

```python
if __name__ == '__main__':
    factory = AnimalFactoryImpl()
    dog = factory.create_animal('Dog')
    cat = factory.create_animal('Cat')
    elephant = factory.create_animal('Elephant')
    
    print(dog.sound())        # Output: Woof
    print(cat.sound())        # Output: Meow
    print(elephant.sound())   # Output: Trumpet
    
```

The output of the program will be:

```
Woof
Meow
Trumpet
```

Conclusion:

In this article, you have learned how to implement the Factory Design Pattern in Python. You now know how to define product interfaces, create concrete products, define factory interfaces, create concrete factories, and test the implementation. By using design patterns like the Factory Design Pattern, you can effectively structure your code and create software that is robust, reusable, and scalable.