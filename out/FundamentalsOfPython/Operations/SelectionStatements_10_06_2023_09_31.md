
selection statements
====================
Hello there! In this tutorial, we'll take you through the basics of using selection statements in Python version 3.10. Selection statements, also known as conditional statements, are an important part of programming. These statements allow you to make decisions in your code based on the value of a variable or expression.

There are two common types of selection statements in Python – the if statement and the switch statement. In this tutorial, we'll focus on the if statement.

Let's dive in!

**Step 1: Understanding the If statement**

The syntax for an if statement in Python is as follows:

```
if condition:
    statement(s)
```

The condition is an expression that evaluates to a boolean value (True or False). If the condition is True, the statement(s) inside the if block will be executed. If the condition is False, the statement(s) inside the if block will be skipped.

**Step 2: Writing your first If statement**

Let's start by writing a simple if statement that prints a message if a variable is greater than 10.

```python
num = 16

if num > 10:
    print("The number is greater than 10")
```

In the example above, we have assigned the value of 16 to the variable num. The if statement checks if num is greater than 10. Since 16 is greater than 10, the message "The number is greater than 10" will be printed.

**Step 3: Adding an else statement**

Sometimes you want to execute a different set of statements if the if condition is False. This is where the else statement comes in. The syntax for an if-else statement is as follows:

```python
if condition:
    statement(s)
else:
    statement(s)
```

Let's modify our previous example to use an else statement.

```python
num = 6

if num > 10:
    print("The number is greater than 10")
else:
    print("The number is less than or equal to 10")
```

In the example above, we have assigned the value of 6 to the variable num. The if statement checks if num is greater than 10. Since 6 is not greater than 10, the else block is executed, and the message "The number is less than or equal to 10" is printed.

**Step 4: Adding an elif statement**

What if you want to check multiple conditions in a single if statement? This is where the elif (short for "else if") statement comes in. The syntax for an if-elif-else statement is as follows:

```python
if condition1:
    statement(s)
elif condition2:
    statement(s)
else:
    statement(s)
```

Let's modify our previous example to use an elif statement.

```python
num = 5

if num > 10:
    print("The number is greater than 10")
elif num > 5:
    print("The number is greater than 5 but less than or equal to 10")
else:
    print("The number is less than or equal to 5")
```

In the example above, we have assigned the value of 5 to the variable num. The if statement checks if num is greater than 10. Since 5 is not greater than 10, the elif condition is checked. The elif condition checks if num is greater than 5. Since 5 is not greater than 5, the else block is executed, and the message "The number is less than or equal to 5" is printed.

**Step 5: Combining if statements with logical operators**

Sometimes you need to check multiple conditions inside a single if statement. This is where logical operators come in. The three common logical operators in Python are AND, OR and NOT.

Here's how you can use them:

```python
if condition1 and condition2:
    statement(s)

if condition1 or condition2:
    statement(s)

if not condition:
    statement(s)
```

The "and" operator returns True if both conditions are True. The "or" operator returns True if either condition is True. The "not" operator returns the opposite boolean value of the condition.

Let's modify our previous example to use logical operators.

```python
num = 7

if num > 10 or num < 5:
    print("The number is outside of the range")
elif num > 5 and num <= 10:
    print("The number is within the range")
else:
    print("Invalid number")
```

In the example above, we have assigned the value of 7 to the variable num. The if statement checks if num is greater than 10 or less than 5. Since 7 is neither greater than 10 nor less than 5, the elif condition is checked. The elif condition checks if num is greater than 5 and less than or equal to 10. Since 7 falls within this range, the message "The number is within the range" is printed.

**Step 6: Conclusion**

Congratulations! You've successfully learned how to use selection statements in Python version 3.10. Selection statements are a powerful tool to help you make decisions in your code based on the values of variables or expressions. You can take these skills and build more complex programs that can make decisions based on a variety of conditions.

Happy coding!