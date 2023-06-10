
object concatenation
====================
Lesson 1: Overview of Object Concatenation 

Object concatenation is an operation that combines multiple objects into a single object. In Python, we can use the 'concatenation operator' (+) to perform this operation. Object concatenation is commonly used for combining two or more strings, but it can also be used for lists, tuples, and other objects that support concatenation.

Lesson 2: Concatenating Strings

To concatenate two or more strings, we use the '+' operator. For example:

```python
str1 = "Hello"
str2 = "world"
combined_str = str1 + str2
print(combined_str)
```

Output:
```
Helloworld
```

We can also concatenate more than two strings at once:

```python
str1 = "Hello"
str2 = "world"
str3 = "!"
combined_str = str1 + str2 + str3
print(combined_str)
```

Output:
```
Helloworld!
```

Lesson 3: Concatenating Lists

We can also concatenate two or more lists using the '+' operator. For example:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)
```

Output:
```
[1, 2, 3, 4, 5, 6]
```

We can also concatenate more than two lists at once:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
combined_list = list1 + list2 + list3
print(combined_list)
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Lesson 4: Concatenating Tuples

Just like lists, we can concatenate two or more tuples using the '+' operator. For example:

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)
```

Output:
```
(1, 2, 3, 4, 5, 6)
```

We can also concatenate more than two tuples at once:

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
combined_tuple = tuple1 + tuple2 + tuple3
print(combined_tuple)
```

Output:
```
(1, 2, 3, 4, 5, 6, 7, 8, 9)
```

Lesson 5: Concatenating Objects of Different Types

We can also concatenate objects of different types, but both objects must support concatenation. For example, we can concatenate a string and a tuple:

```python
str1 = "Hello "
tuple1 = ("world", "!")
combined_obj = str1 + tuple1[0] + tuple1[1]
print(combined_obj)
```

Output:
```
Hello world!
```

However, we cannot concatenate a string and a number because they do not support concatenation:

```python
str1 = "Hello "
num1 = 6
combined_obj = str1 + num1
print(combined_obj)
```

Output:
```
TypeError: can only concatenate str (not "int") to str
```

Lesson 6: Using Object Concatenation in Loops

Object concatenation can be very useful when used in loops. For example:

```python
my_list = ["apple", "banana", "pear"]
combined_str = ""
for item in my_list:
    combined_str += item + ", "
print(combined_str[:-2])
```

Output:
```
apple, banana, pear
```

In this example, we used object concatenation to combine all the items in a list into a single string separated by commas.

Lesson 7: Conclusion

Object concatenation can be very useful when we need to combine two or more objects into a single object. We can use the '+' operator to perform concatenation on strings, lists, tuples, and other objects that support concatenation. Remember: Both objects must support concatenation in order to be concatenated.