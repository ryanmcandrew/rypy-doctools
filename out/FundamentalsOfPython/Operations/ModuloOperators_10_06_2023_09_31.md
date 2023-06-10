
modulo operators
================
Lesson 1: Understanding the modulo operator
One of the basic concepts in programming is arithmetic operators. In Python, the modulo operator is represented by a percent symbol (%). The modulo operator gives us the remainder of a division operation. So, if we have two numbers, a and b, the modulo operator gives us a number that represents what is remaining after dividing a by b. 
For example, if we have 7%3, the modulo operator will give us 1 as the remainder of dividing 7 by 3. 

Lesson 2: Using the modulo operator in Python
Now that we understand what the modulo operator does, let's learn how to use it in Python. The usage of the modulo operator is quite simple. We just use the % sign between the numbers we want to divide. For example, 7%3 will give us the answer of 1. 

Lesson 3: Modulo with even and odd numbers
A modulo operation can be used to determine whether a number is even or odd. An even number will always produce a remainder of 0 when divided by 2. An odd number will always produce a remainder of 1 when divided by 2. Let’s try this with Python. 

number = 10
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

Here we set the number as 10, and we’re checking to see whether the number divided by 2 has a remainder of 0. Since 10 is even, its modulo will be 0. Therefore, the output of the code will be “The number is even”. 

Lesson 4: Modulo for checking leap years
A leap year is a year that is divisible by 4. However, if the year is divisible by 100, then it is not a leap year unless it is also divisible by 400. Here’s a Python code that checks whether a year is a leap year. 

year = 2024
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))

Here the year is set as 2024. We start with checking if the year is divisible by 4. If yes, we move on to checking if the year is divisible by 100 to determine if it’s a century year. If it is, we then check if it’s also divisible by 400, meaning a leap year. If it’s not a century year, we conclude it is a leap year. Therefore it will return “2024 is a leap year”. If the year was not a leap year it would have returned “2024 is not a leap year”. 

Lesson 5: Modulo with negative numbers
Another thing to note is that modulo can sometimes behave differently with negative numbers compared to positive numbers. Here’s a table from the Python documentation that shows how modulo works with positive and negative values: 

a  b  a % b
3  2  1
-3 2  1
3  -2 1
-3 -2 -1

As we see here, we will always get the correct answer regardless of the positive or negative. 

Conclusion:
In this course, we have learned what the modulo operator is, how to use it in Python by using different examples, such as checking whether a number is even or odd and finding out leap years. We have also learned how modulo works with negative numbers. Keep practicing using modulo operations to build up your skills!