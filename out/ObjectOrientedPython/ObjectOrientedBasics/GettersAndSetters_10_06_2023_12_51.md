
getters and setters
===================
Introduction:
Getters and setters are a way of accessing and modifying the private or protected attributes of a class. An attribute is considered private when it is declared with two underscores ' __' before the name. In Python, the concept of private attributes is not strict as the language does not provide any access modifiers like public, private, or protected. Getters and setters can be used to make private attributes accessible. In this tutorial, we will learn how to use getters and setters in Python 3.10.

Step 1: Define a class
Let's start by defining a class that will have some private attributes.

```python
class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade
```
The above class has three attributes - name, age, and grade. All these attributes are private as they have double underscores before their names.

Step 2: Define getters and setters
We need to define getters and setters for all the private attributes so that they can be accessed and modified from outside the class.

```python
class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        self.__grade = grade
```
In the above code, we have defined getters and setters for all the private attributes.
- get_name() returns the name of the student.
- set_name() sets the name of the student.
- get_age() returns the age of the student.
- set_age() sets the age of the student.
- get_grade() returns the grade of the student.
- set_grade() sets the grade of the student.

Step 3: Accessing and modifying attributes using getters and setters
Now, we can use the getters and setters to access and modify the attributes of the instance of the class.

```python
s = Student("John", 18, "A")

print(s.get_name())   # Output: John
print(s.get_age())    # Output: 18
print(s.get_grade())  # Output: A

s.set_name("Marry")
s.set_age(20)
s.set_grade("B")

print(s.get_name())   # Output: Marry
print(s.get_age())    # Output: 20
print(s.get_grade())  # Output: B
```

In the above code, we have created an instance of the class Student and accessed its attributes using getters and setters. We also modified the attributes using setters.

Conclusion:
Getters and setters are important parts of object-oriented programming. They allow us to access and modify the private attributes of a class in a controlled way. In Python, there are no access modifiers like public, private, or protected. However, we can achieve the functionality of these access modifiers using the concept of get and set methods.