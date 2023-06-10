
interface design patterns
=========================
Introduction:
Interface design patterns are a set of principles that are used to provide interface solutions to common design issues that arise in software programming. In this course, we will explore some of the most common interface design patterns used in Python version 3.10.

Objectives:
The main objectives of this course are:
• Understanding the concept of interface design patterns
• Exploring common interface design patterns used in Python 3.10
• Learning to implement interface design patterns in Python 3.10

Requirements:
• Python version 3.10 installed on your computer
• Basic knowledge of Python programming language
• Knowledge of object-oriented programming

Course outline:
• Introduction to interface design patterns
• Factory design pattern
• Singleton design pattern
• Adapter design pattern
• Decorator design pattern
• Facade design pattern
• Conclusion

Introduction to interface design patterns:
Interface design patterns are a set of principles that are used to provide interface solutions to common design issues that arise in software programming. Interface design patterns help developers to write more readable, maintainable, and reusable code.

Some of the common interface design patterns used in Python version 3.10 are:
• Factory design pattern
• Singleton design pattern
• Adapter design pattern
• Decorator design pattern
• Facade design pattern

In this course, we will explore each of these design patterns and learn how to implement them in Python 3.10.

Factory design pattern:
The factory design pattern is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. The factories are used when the creation of an object directly is expensive or complicated.

To implement the factory design pattern in Python 3.10, we need to follow the steps below:
1. Create an abstract base class that defines the interface for all the products that the factory is going to produce.
2. Create different types of concrete classes that implement the same interface.
3. Create a factory that provides an interface to create an object of a type required by the client.

Example code:
```
from abc import ABC, abstractmethod

class Door(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

class WoodenDoor(Door):
    def open(self):
        print("The wooden door is opened.")

    def close(self):
        print("The wooden door is closed.")

class IronDoor(Door):
    def open(self):
        print("The iron door is opened.")

    def close(self):
        print("The iron door is closed.")

class DoorFactory:
    @staticmethod
    def make_door(material):
        if material == "wood":
            return WoodenDoor()
        elif material == "iron":
            return IronDoor()
        else:
            raise ValueError("Unknown door type.")

door = DoorFactory.make_door("wood")
door.open()
door.close()
```

Singleton design pattern:
The singleton design pattern is a creational pattern that restricts the instantiation of a class to only one object. The singleton is used when only one instance of the class should exist.

To implement the singleton design pattern in Python 3.10, we need to follow the steps below:
1. Create a class that has a private constructor.
2. Create a static method that returns the instance of the class.
3. Create a static variable to store the instance of the class.

Example code:
```
class Database:
    __instance = None

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Only one instance of the singleton class is allowed.")
        else:
            Database.__instance = self

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance
```

Adapter design pattern:
The adapter design pattern is a structural pattern that allows two incompatible interfaces to work together. The adapter is used when the interface of an existing class does not match the interface required by the client.

To implement the adapter design pattern in Python 3.10, we need to follow the steps below:
1. Create an abstract class or interface that defines the required interface.
2. Create a class that implements the required interface.
3. Create an adapter class that implements the required interface and accepts the incompatible class as an argument.

Example code:
```
from abc import ABC, abstractmethod

class IRectangle(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self):
        pass

class Rectangle(IRectangle):
    def draw(self):
        print("Drawing rectangle.")

    def resize(self):
        print("Resizing rectangle.")

class Circle:
    def draw_circle(self):
        print("Drawing circle.")

class CircleAdapter(IRectangle):
    def __init__(self, circle):
        self.circle = circle

    def draw(self):
        self.circle.draw_circle()

    def resize(self):
        print("Resizing circle.")

circle = Circle()
circle_adapter = CircleAdapter(circle)
circle_adapter.draw()
circle_adapter.resize()
```

Decorator design pattern:
The decorator design pattern is a structural pattern that allows adding new functionality to an existing object without altering its structure. The decorator is used when the client needs to dynamically add new functionality to an object.

To implement the decorator design pattern in Python 3.10, we need to follow the steps below:
1. Create an abstract class or interface that defines the required interface.
2. Create a concrete class that implements the required interface.
3. Create a decorator class that extends the original class and adds new functionality.

Example code:
```
from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(IShape):
    def draw(self):
        print("Drawing circle.")

class ShapeDecorator(IShape):
    def __init__(self, decorated_shape):
        self.decorated_shape = decorated_shape

    def draw(self):
        self.decorated_shape.draw()

class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decorated_shape):
        super().__init__(decorated_shape)

    def draw(self):
        self.decorated_shape.draw()
        self.set_red_border()

    def set_red_border(self):
        print("Border color is set to red.")

circle = Circle()
decorated_circle = RedShapeDecorator(circle)
decorated_circle.draw()
```

Facade design pattern:
The facade design pattern is a structural pattern that simplifies the interface of complex subsystems. The facade is used when a client needs to access a complex system that has many different interfaces.

To implement the facade design pattern in Python 3.10, we need to follow the steps below:
1. Create a facade class that provides a simple interface to the complex subsystem.
2. Create a complex subsystem that has many different interfaces.

Example code:
```
class SubsystemA:
    def method_a1(self):
        print("Method A1 is called.")

    def method_a2(self):
        print("Method A2 is called.")

class SubsystemB:
    def method_b1(self):
        print("Method B1 is called.")

    def method_b2(self):
        print("Method B2 is called.")

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def do_something(self):
        self.subsystem_a.method_a1()
        self.subsystem_b.method_b1()
```

Conclusion:
Interface design patterns are essential for writing readable, maintainable, and reusable code. The Python programming language provides many interface design patterns that help developers to solve common design issues. In this course, we have explored the factory, singleton, adapter, decorator, and facade design patterns and learned how to implement them in Python version 3.10.