
loops of the form: for i in array
=================================
How to use loops of the form "for i in array" in Python version 3.10

In Python, loops are used to iterate through a series of data, commonly known as an array or a list. The "for i in array" loop is one of many different types of loops that Python has to offer. In this course, we will focus on how to use loops of the form "for i in array" in Python version 3.10.

Step 1: Understanding the syntax of "for i in array" loop

The syntax for a "for i in array" loop is as follows:

```python
for i in array:
   # do something with i
```

The loop starts by iterating through the elements of the array, assigning each element to the variable "i" one at a time. The code inside the loop block is then executed with the value of "i". Once the code has been executed for all elements of the array, the loop ends.

Step 2: Creating an array

In order to test the "for i in array" loop, we first need to create an array. Here's how to create an array in Python:

```python
array = ["apple", "banana", "cherry"]
```

This creates an array of three elements: "apple", "banana", and "cherry".

Step 3: Using a "for i in array" loop to iterate through the array

Now that we have an array to work with, we can use a "for i in array" loop to iterate through the elements of the array and perform some action as we go. Here's an example:

```python
for i in array:
   print(i)
```

This code will iterate through the elements of the array, printing each element to the console as it goes. The output will look like this:

```
apple
banana
cherry
```

Step 4: Using the loop variable in the loop block

In the loop block, we can use the loop variable "i" to perform some action on each element of the array. Here's an example that counts the number of letters in each element of the array:

```python
for i in array:
   print(len(i))
```

This code will iterate through the elements of the array, printing the length of each element to the console as it goes. The output will look like this:

```
5
6
6
```

Step 5: Conclusion

In this course, we covered the basics of using loops of the form "for i in array" in Python version 3.10. We discussed the syntax of the loop, how to create an array, and how to use the loop variable "i" in the loop block. With this knowledge, you can create more complex loops to iterate through arrays and perform useful actions on each element.