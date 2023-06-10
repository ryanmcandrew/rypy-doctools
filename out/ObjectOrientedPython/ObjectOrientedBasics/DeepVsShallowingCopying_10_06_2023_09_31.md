
deep vs shallowing copying
==========================
Title: How to Use Deep vs Shallow Copying in Python Version 3.10

Introduction:
Python is a flexible and versatile programming language that offers two types of copying: deep copy and shallow copy. Both are used to clone objects in Python, but with different levels of copying. In this course, we will discuss the difference between deep and shallow copying and how to use them in Python version 3.10.

Prerequisites:
Basic knowledge of Python programming language including understanding of data types, control structures, functions, and classes.

Lesson 1: What is Deep Copying in Python?
In Python, deep copying involves copying the entire object hierarchy. In other words, it creates a new object with a complete copy of the original object and all its contents. This means that any changes made to the copied object will not affect the original object. 

Example: 
Copy List using Deep Copy
```
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new = original.copy()
original[0][0] = 0
print(new) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
Copy List using Deep Copy and copy.deepcopy()
```
import copy
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new = copy.deepcopy(original)
original[0][0] = 0
print(new) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Lesson 2: What is Shallow Copying in Python?
In Python, shallow copying involves only copying the top-level object and any references to nested objects. In other words, it does not create a complete copy of the original object and all its contents. Instead, it creates a new object that points to the original object's nested objects. This means that any changes made to the nested objects in the copied object will affect the original object.

Example: 
Copy List using Shallow Copy
```
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new = original.copy()
original[0][0] = 0
print(new) # Output: [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
```
Copy List using Shallow Copy and copy.copy()
```
import copy
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new = copy.copy(original)
original[0][0] = 0
print(new) # Output: [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Lesson 3: How to Use Deep Copying in Python
To use deep copying in Python, we can use the built-in 'copy' module and 'deepcopy' sub-module. The module contains two functions:
- copy.copy(): performs shallow copying
- copy.deepcopy(): performs deep copying

Example: 
```
import copy
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new = copy.deepcopy(original)
```

Note: We must import the 'copy' module to use these functions.

Lesson 4: How to Use Shallow Copying in Python
To use shallow copying in Python, we can use the built-in 'copy' module. The module contains two functions:
- copy.copy(): performs shallow copying
- copy.deepcopy(): performs deep copying

Example: 
```
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new = original.copy()
```

Note: We must import the 'copy' module to use copy() function for shallow copy.

Lesson 5: When to Use Deep Copying vs Shallow Copying
Deep copying provides a complete copy of the original object and all of its contents. It is ideal when we need to modify the copied object without affecting the original object. However, it can be time-consuming and may not be efficient for large and complex objects. 

Shallow copying provides a faster and more efficient way to clone objects. However, it does not provide a complete copy of the original object and may affect the original object when nested objects are modified.

Conclusion:
In this How-To course, we have learned the difference between deep and shallow copying and how to use them in Python version 3.10. While both are used to clone objects in Python, they are used with different levels of copying. We have also learned when to use deep copying versus shallow copying and their advantages and disadvantages.