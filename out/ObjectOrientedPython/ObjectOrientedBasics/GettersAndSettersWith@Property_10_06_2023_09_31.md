
getters and setters with @property
==================================
Introduction:

Getters and setters are methods used in object-oriented programming languages to manage the access to class attributes or data members. In Python, we use the @property decorator to define getters and setters. Python 3.10 introduced some new features that make working with properties even easier. This course will explain how to use getters and setters with @property in Python 3.10.

Step 1: Defining a Class

Before you can start using getters and setters, you need to define a class. For this example, we will use a class named Person with two attributes: name and age.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
```

In this example, we have used the __init__ method to initialize the name and age attributes of a person.

Step 2: Defining Getter Methods

Now that we have defined the class, we can define getter methods. A getter method is a method used to retrieve the value of a private attribute.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
```

In this example, we have defined two getter methods for the name and age attributes. We use the @property decorator to define these methods.

Step 3: Defining Setter Methods

Now that we have defined the getter methods, we can define setter methods. A setter method is a method used to set the value of a private attribute.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
```

In this example, we have defined setter methods for the name and age attributes. We use the @propertyName.setter decorator to define these methods.

Step 4: Using Getter and Setter Methods

Now that we have defined the getter and setter methods, we can use them to retrieve and set the value of the name and age attributes.

```python
person = Person("John", 30)
print(person.name)  # Output: John
print(person.age)  # Output: 30

person.name = "David"
person.age = 40
print(person.name)  # Output: David
print(person.age)  # Output: 40
```

In this example, we have created an instance of the Person class with the name "John" and age 30. We have used the getter methods to retrieve the current value of the name and age attributes. We have used the setter methods to set the value of the name and age attributes to "David" and 40, respectively.

Conclusion:

Getters and setters are an important part of object-oriented programming. In Python 3.10, we can use the @property decorator to define getter and setter methods. With these methods, you can control the access to the attributes of your classes and ensure that they are used correctly.