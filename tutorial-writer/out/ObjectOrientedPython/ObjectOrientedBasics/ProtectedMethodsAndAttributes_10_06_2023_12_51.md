
protected methods and attributes
================================
Introduction:

In Python version 3.10, method and attributes can be protected with a single leading underscore, which means that they're private and not accessible outside of the class, but they still can be accessed inside the class and any child classes. This can be useful to avoid accidental modification and to keep critical data encapsulated.

In this how-to course, we will explore how to use protected methods and attributes in Python 3.10.

Step 1: Creating a class with protected methods and attributes

To start, let's create a simple class with protected methods and attributes.

```python
class MyClass:
    def __init__(self, _protected_attr):
        self._protected_attr = _protected_attr
    
    def _protected_method(self):
        print("This is a protected method.")
```

In this example, we have a class named MyClass, with a constructor that takes a protected attribute named _protected_attr, and a protected method named _protected_method.

Note that the name convention for protected attributes and methods is to prefix them with a single underscore.

Step 2: Accessing protected methods and attributes within the class

Now that we have a class with protected methods and attributes, let's try to access them within the class.

```python
class MyClass:
    def __init__(self, _protected_attr):
        self._protected_attr = _protected_attr
    
    def _protected_method(self):
        print("This is a protected method.")

    def access_protected_attr(self):
        print("The protected attribute is:", self._protected_attr)
        
        print("Calling the protected method...")
        self._protected_method()
```

In this example, we have added a new method named access_protected_attr that prints the value of the protected attribute and calls the protected method.

Note that accessing protected attributes and methods inside the class is allowed and can help you to reuse the code.

Step 3: Using protected methods and attributes from a child class

Now that we can access protected methods and attributes within the class, let's see how to use them from a child class.

```python
class ChildClass(MyClass):
    def __init__(self, _protected_attr):
        MyClass.__init__(self, _protected_attr)
    
    def call_protected_method_from_parent(self):
        print("Calling the protected method from the parent...")
        self._protected_method()
```

In this example, we have created a child class named ChildClass that inherits from MyClass and adds a new method named call_protected_method_from_parent that calls the protected method from the parent class.

Note that child classes can access protected attributes and methods from their parent class.

Step 4: Accessing protected methods and attributes outside of the class

Finally, let's try to access protected methods and attributes from outside of the class.

```python
a = MyClass("Hello World")
a.access_protected_attr()
a._protected_attr = "Modified!"
a.access_protected_attr()
a._protected_method()
```

In this example, we have created an instance of MyClass named a and called the access_protected_attr method to get the value of the protected attribute.

Then we changed the value of the protected attribute by accessing it directly, which is allowed but not recommended.

Finally, we tried to call the protected method from outside of the class, but this is not allowed and will generate an AttributeError since protected methods and attributes are not accessible from outside of the class and its child classes.

Conclusion:

Using protected methods and attributes can be a useful technique to encapsulate data and avoid accidental modification, but it should not be used as a security measure since it is not enforced by the interpreter. Protected attributes and methods can still be accessed outside of the class, but the underscore prefix serves as a convention to signal that they're private and should not be used without understanding their implications.