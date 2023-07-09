
selection statements
====================
Welcome to the course on using selection statements in Python version 3.10. In this course, we will explore the basics of selection statements and learn how to use them in Python to make decisions that will help our programs function more efficiently.

Before we begin, it is important to understand that selection statements are conditional statements that allow us to execute specific code depending on whether a particular condition is true or false. There are two types of selection statements in Python:

- If statements
- If-else statements

If statements

An if statement executes a specific block of code if a certain condition is true. The basic syntax of an if statement looks like this:

```
if condition:
    # code to execute if condition is true
```

Here's a simple example:

```
x = 10
if x > 5:
    print("x is greater than 5")
```

In this example, the condition is `x > 5`. Since this condition is true (because `x` is equal to 10, which is greater than 5), the code inside the if statement is executed and "x is greater than 5" is printed to the console.

If-else statements

An if-else statement, on the other hand, executes a different block of code depending on whether a certain condition is true or false. The basic syntax of an if-else statement looks like this:

```
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

Here's a simple example:

```
x = 2
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

In this example, the condition is `x > 5`. Since this condition is false (because `x` is equal to 2, which is less than 5), the code inside the else statement is executed and "x is less than or equal to 5" is printed to the console.

Now that we know the basics of selection statements, let's dive into some more advanced concepts.

Nested if statements

Sometimes we need to perform multiple checks before making a decision. We can achieve this by using nested if statements. A nested if statement is simply an if statement inside another if statement. Here's an example:

```
x = 10
y = 5
if x > 5:
    if y > 2:
        print("x is greater than 5 and y is greater than 2")
```

In this example, we are checking whether `x` is greater than 5 and whether `y` is greater than 2. Since both conditions are true, the code inside the nested if statement is executed and "x is greater than 5 and y is greater than 2" is printed to the console.

Logical operators

Sometimes we need to check multiple conditions at the same time. We can achieve this using logical operators. There are three main logical operators in Python:

- and
- or
- not

The `and` operator returns True if both conditions are True. The `or` operator returns True if at least one of the conditions is True. The `not` operator negates the condition. Here's an example:

```
x = 10
y = 5
if x > 5 and y > 2:
    print("x is greater than 5 and y is greater than 2")
```

In this example, we are using the `and` operator to check whether both conditions are true. Since both conditions are true (because `x` is equal to 10 and `y` is equal to 5, which is greater than 2), the code inside the if statement is executed and "x is greater than 5 and y is greater than 2" is printed to the console.

Conclusion

In this course, we have explored the basics of selection statements and learned how to use if and if-else statements in Python. We have also looked at more advanced concepts such as nested if statements and logical operators. By applying what you have learned in this course, you can make your Python programs more efficient and effective.