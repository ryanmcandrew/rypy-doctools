
ternary operators
=================
Lesson Title: Using Ternary Operators in Python 3.10

Introduction:
Ternary operators are a concise and efficient way of writing conditional statements in Python. They save time and make your code look cleaner and more readable. In this course, you will learn how to use ternary operators in Python 3.10.

Lesson Objectives:
- Understand what ternary operators are and their syntax in Python 3.10.
- Know when and how to use ternary operators in Python 3.10.
- Practice writing ternary operators for different types of conditions.

Lesson Body:

1. What are Ternary Operators?
Ternary operators are conditional expressions that evaluate a Boolean expression and return one of two values depending upon the result of the evaluation. In Python 3.10, the syntax for ternary operators is as follows: 

value_if_true if condition else value_if_false 

where:
- value_if_true is what will be returned if the condition is true
- condition is the assertion to be tested
- value_if_false is what will be returned if the condition is false

2. Examples of Ternary Operators
Here are some examples of ternary operators in Python 3.10:

# Example 1: 
# Set variable x to value 5 if y is greater than 10, otherwise set x to value 10 

x =  5 if y > 10 else 10 

# Example 2: 
# Print "positive" if variable x is greater than 0, otherwise print "non-positive"

print("positive" if x > 0 else "non-positive")

# Example 3:
# Set variable color to "red" if the variable fruit is "apple", 
# "green" if the variable fruit is "watermelon", otherwise set color to "yellow"

color = "red" if fruit == "apple" else "green" if fruit == "watermelon" else "yellow"

3. When and How to Use Ternary Operators
Ternary operators are useful when you have a simple condition that can be resolved to one of two possible values. You should use them when you want to make your code more concise and readable.

To use ternary operators, start by defining your condition and then put the value to be returned if the condition is true before the 'if' keyword. Then, put the value to be returned if the condition is false after the 'else' keyword.

If the condition is complex or the values are complex, it's better to use 'if-else' statements instead of ternary operators.

4. Practice Writing Ternary Operators
Now that you understand the syntax and usage of ternary operators, start practicing by writing some of your own. Here are a few exercises to get you started:

a. Write a ternary operator that sets the variable 'discount' to 10% if the variable 'total_cost' is greater than 100, otherwise set 'discount' to 5%.

b. Write a ternary operator that sets the variable 'grade' to 'A' if 'score' is greater than or equal to 90, 
   'B' if 'score' is greater than or equal to 80, and 'C' if 'score' is greater than or equal to 70, otherwise set 'grade' to 'D'.

c. Write a ternary operator that sets the variable 'message' to 'it's a weekday' if the variable 'day' is a weekday (Monday to Friday), otherwise set 'message' to 'it's a weekend!'.

Conclusion:
Ternary operators are a simple and effective alternative to 'if-else' statements in many situations. They are easy to use and can make your code more readable. Practice using them in different types of code and choose the most adequate in every situation.