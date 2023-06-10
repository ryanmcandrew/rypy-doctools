
nested functions
================
Introduction:

Python is a very versatile language, and one of its most powerful features is the ability to use nested functions. This feature allows us to create functions within other functions. In this course, we will learn how to use nested functions in Python version 3.10.

Lesson 1: Understanding Nested Functions

Nested functions are just normal functions that are created within another function. They can access variables and parameters of the parent function, and they can be called from within the parent function.

Here is an example of a simple nested function:

```
def outer_function():
    
    def inner_function():
        print("Hello from inner function!")
    
    inner_function()

outer_function()
```

When we run the above program, it will output "Hello from inner function!" on the console. As you can see, we have created a nested function called inner_function() within the outer_function().

Lesson 2: Passing Arguments to Nested Functions

Nested functions can be passed arguments just like any other function. Here is an example:

```
def outer_function(name):
    
    def inner_function():
        print("Hello from inner function, " + name + "!")
    
    inner_function()

outer_function("John")
```

When we run this program, it will output "Hello from inner function, John!" on the console.

As you can see, we have passed an argument called "name" to the outer_function(). This argument is then used in the nested function called inner_function().

Lesson 3: Returning Values from Nested Functions

We can also return values from nested functions. Here is an example:

```
def outer_function(name):
    
    def inner_function():
        return "Hello from inner function, " + name + "!"
    
    return inner_function()

result = outer_function("John")
print(result)
```

When we run this program, it will output "Hello from inner function, John!" on the console.

As you can see, we have returned the value of the nested function called inner_function() to the outer_function(). The outer_function() then returns this value to the main program, which prints it on the console.

Lesson 4: Using Lambda Functions as Nested Functions

We can also use lambda functions as nested functions. Here is an example:

```
def outer_function():
    
    inner_function = lambda x: x * 2
    
    return inner_function(5)

result = outer_function()
print(result)
```

When we run this program, it will output 10 on the console.

As you can see, we have created a lambda function called inner_function() within the outer_function(). This lambda function takes an argument and multiplies it by 2. The outer_function() then returns the result of this lambda function to the main program, which prints it on the console.

Conclusion:

Nested functions are a powerful feature of Python that allow us to create functions within other functions. They can be used to pass arguments, return values, and even use lambda functions. By mastering nested functions, we can write more concise and efficient code in Python.