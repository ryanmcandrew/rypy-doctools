
getters and setters
===================
Introduction:
Getters and setters are used in code to control the way data is accessed, manipulated, or modified. They allow developers to ensure the proper operation of code by preventing unauthorized access or modification of data by external entities. In this course, you will learn how to use getters and setters in Python version 3.10

Prerequisites:
To complete this course, you need to have a basic understanding of Object-Oriented Programming (OOP) concepts in Python.

Getting started:
Let's create a simple class, and we will use getters and setters in it.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
```

Here, we have created a class called Person. It has two attributes, name and age. To access these attributes from outside the class, we need to define a getter and a setter.

Getters:
Getters are used to access the value of an attribute from outside the class. To define a getter, we use the `@property` decorator.

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

Here, we have defined two getters, one for name and one for age. We can access these attributes using dot notation, even though they are private:

```python
person = Person("John", 30)
print(person.name)
print(person.age)
```

The output will be:
```
John
30
```

Setters:
Setters are used to set the value of an attribute from outside the class. To define a setter, we use the `@<attribute>.setter` decorator.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self._age = new_age
```

Here, we have defined two setters, one for name and one for age. We can now set the attributes using dot notation, even though they are private:

```python
person = Person("John", 30)
person.name = "Jack"
person.age = 35
```

We can also raise an exception if the value being set is not acceptable:

```python
person.age = -5
```

This will raise a ValueError with the message "Age cannot be negative".

Conclusion:
Getters and setters are very important in OOP, especially in Python. By using them, we can control how data is accessed, manipulated, or modified. In this course, we learned how to use getters and setters in Python version 3.10.