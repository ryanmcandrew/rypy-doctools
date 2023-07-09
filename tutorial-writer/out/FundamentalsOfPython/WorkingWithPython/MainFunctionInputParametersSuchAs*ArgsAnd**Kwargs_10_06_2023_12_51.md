
main function input parameters such as *args and **kwargs
=========================================================
In Python, 'args' and 'kwargs' are used as parameters in the main function to pass a variable number of arguments to the function. In this how-to course, we will discuss how you can use these two parameters in your Python program with code examples.

Using '*args' in Python 3.10:

The '*' operator is used to define 'args' in Python. It allows us to pass a variable number of arguments to the function.

Consider the following example:

```
def print_fruit(*args):
    for fruit in args:
        print(fruit)
        
print_fruit('Apple', 'Banana', 'Mango', 'Pear')
```

Output:

```
Apple
Banana
Mango
Pear
```

In the above example, we have defined a function 'print_fruit' that accepts any number of arguments. We have passed four different fruit names as arguments to the function. Inside the function, the 'for' loop iterates over all the arguments and prints them one by one.

Using '**kwargs' in Python 3.10:

The '**' operator is used to define 'kwargs' in Python. It allows us to pass a variable number of keyword arguments to the function.

Consider the following example:

```
def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
print_data(name='John', age=25, country='USA')
```

Output:

```
name: John
age: 25
country: USA
```

In the above example, we have defined a function 'print_data' that accepts any number of keyword arguments. We have passed three different keyword arguments, i.e., name, age, and country, to the function. Inside the function, the 'for' loop iterates over all the keyword arguments and prints them along with their corresponding values.

Using both '*args' and '**kwargs' in Python 3.10:

We can also use both '*args' and '**kwargs' together in a function. In such cases, '*args' should come before '**kwargs'.

Consider the following example:

```
def print_details(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
print_details('John', 25, 'USA', email='john@example.com', phone='12345')
```

Output:

```
John
25
USA
email: john@example.com
phone: 12345
```

In the above example, we have defined a function 'print_details' that accepts both positional arguments and keyword arguments. We have passed three positional arguments, i.e., name, age, and country, and two keyword arguments, i.e., email and phone, to the function. Inside the function, the first 'for' loop iterates over all the positional arguments and prints them. The second 'for' loop iterates over all the keyword arguments and prints them along with their corresponding values.

Conclusion:

In Python 3.10, '*args' and '**kwargs' are very useful features that allow us to write flexible and reusable code. By using these parameters, we can pass a variable number of arguments to a function, making our code more dynamic and efficient.