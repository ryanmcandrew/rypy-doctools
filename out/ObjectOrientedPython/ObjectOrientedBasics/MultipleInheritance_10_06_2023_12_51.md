
multiple inheritance
====================
Lesson 1: Understanding the concept of multiple inheritance

In Python, multiple inheritance is the ability of a class to inherit properties and behavior from multiple parent classes.

For example, you can create a sub-class that inherits from two or more base classes. This allows you to reuse code and reduce duplication.

Lesson 2: Creating a class with multiple inheritance

To create a class with multiple inheritance, you need to specify the base classes in the class definition.

Here's an example:

```
class A:
    def foo(self):
        print('A.foo')

class B:
    def bar(self):
        print('B.bar')

class C(A, B):
    pass
```

In this example, we have three classes:

- `A`, with a method `foo()`.
- `B`, with a method `bar()`.
- `C`, which inherits from both `A` and `B`.

The `pass` statement in the `C` class means that it doesn't have any additional methods or attributes.

Lesson 3: Calling methods from parent classes

When you have a class with multiple inheritance, you can call methods from its parent classes.

Here's an updated example:

```
class A:
    def foo(self):
        print('A.foo')

class B:
    def bar(self):
        print('B.bar')

class C(A, B):
    def baz(self):
        self.foo()
        self.bar()
```

In the `C` class, we've added a method `baz()` that calls both `foo()` and `bar()` from its parent classes.

Lesson 4: Solving method resolution order conflicts

The order of base classes matters in Python. If a class inherits from two or more classes with the same method name, Python uses the method from the first class specified in the inheritance list.

For example:

```
class A:
    def hello(self):
        print('A')

class B:
    def hello(self):
        print('B')

class C(B, A):
    pass

c = C()
c.hello()
```

In this example, the `C` class inherits from both `A` and `B`, and they both have a method named `hello()`. But because `B` is listed before `A` in the inheritance list, `C` uses the `hello()` method from `B`.

If you want to specify a different method order, you can use the `super()` function to call the method from the next class in the inheritance list.

For example:

```
class A:
    def hello(self):
        print('A')

class B:
    def hello(self):
        print('B')

class C(A, B):
    def hello(self):
        super().hello()
        super(B, self).hello()

c = C()
c.hello()
```

In this example, the `C` class has a method `hello()` that calls `super().hello()`, which is equivalent to calling `A.hello()`. It then calls `super(B, self).hello()`, which is equivalent to calling `B.hello()`. This lets you control the order of method resolution.

Lesson 5: Understanding diamond inheritance

Diamond inheritance is a situation where a class inherits from two classes that have a common ancestor.

For example:

```
class A:
    def hello(self):
        print('A')

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.hello()
```

In this example, the `D` class inherits from both `B` and `C`, which both inherit from `A`. This creates a diamond-shaped inheritance structure.

When you call a method on an instance of `D`, Python searches for the method in this order:

1. `D`
2. `B`
3. `C`
4. `A`

Because both `B` and `C` inherit from `A`, Python ends up searching for `hello()` twice in the search order, which can cause unexpected behavior.

To avoid this, you can use a technique called method resolution order (MRO), which is a way to determine the order in which methods are searched for in a diamond inheritance structure.

```
class A:
    def hello(self):
        print('A')

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

In this example, we've added a `print()` statement that calls `mro()` on the `D` class. This returns a tuple of the method resolution order, which in this case is `(D, B, C, A)`. This tells Python to search for methods in this order, which ensures that each method is called only once.

Conclusion:

Python's multiple inheritance feature lets you create complex class hierarchies by inheriting from multiple base classes. By using super() method, resolving method resolution conflicts etc we can utilize python multiple inheritance.