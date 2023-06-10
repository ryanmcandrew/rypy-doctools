
protected methods and attributes
================================
How to Use Protected Methods and Attributes in Python 3.10

In object-oriented programming, encapsulation is a powerful design principle that helps to keep the complexity of your code under control. Encapsulation allows you to hide the implementation details of your objects and expose only the necessary functionality to the outside world. In Python, you can use protected methods and attributes to help implement encapsulation.

Protected methods and attributes are a way to indicate that certain methods and attributes should not be used outside of the class definition or its subclasses. By convention, a method or attribute that starts with a single underscore (_) is considered protected. Let's take a look at how to use protected methods and attributes in Python 3.10.

Step 1: Define a Class

To get started, define a class that will contain your protected methods and attributes. Here's an example:

```
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
 
    def _get_name(self):
        return self._name
 
    def _get_age(self):
        return self._age
```

In this example, we have defined a Person class with two protected attributes: _name and _age. We have also defined two protected methods: _get_name() and _get_age(). 

Step 2: Accessing Protected Methods and Attributes

Accessing protected methods and attributes within the class definition is straightforward: simply use the method or attribute name as usual. For example, to access the _name attribute in the Person class, we can use code like this:

```
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
 
    def _get_name(self):
        return self._name
 
    def _get_age(self):
        return self._age
 
    def get_info(self):
        name = self._get_name()
        age = self._get_age()
        return f"{name} is {age} years old."
```

In this example, we have added a new method called get_info() which uses the _get_name() and _get_age() methods to return a string with the person's name and age.

Step 3: Making the Class Inaccessible from Outside

To make the Person class inaccessible from outside, you can add a double underscore (_) before the class name. This will effectively hide the class from external access. Here's how to modify the Person class to use double underscores:

```
class __Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
 
    def _get_name(self):
        return self._name
 
    def _get_age(self):
        return self._age
 
    def get_info(self):
        name = self._get_name()
        age = self._get_age()
        return f"{name} is {age} years old."
```

In this modified class, the __Person class is now hidden from external access. You can still create instances of the Person class by using a subclass, like this:

```
class Person(__Person):
    def __init__(self, name, age):
        super().__init__(name, age)
```

This code creates a new Person class that inherits from the __Person class. You can now create instances of the Person class, but you cannot create instances of the __Person class directly.

Conclusion

Using protected methods and attributes can help you to implement encapsulation in your Python code, allowing you to hide implementation details from the outside world. By convention, a method or attribute that starts with a single underscore (_) is considered protected. With this guide, you should now have a good foundation for using protected methods and attributes in Python 3.10.