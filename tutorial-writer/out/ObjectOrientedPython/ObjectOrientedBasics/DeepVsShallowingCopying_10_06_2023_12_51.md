
deep vs shallowing copying
==========================
Introduction:

In Python, when we work with objects, we often need to create copies of them. Copying objects refers to the process of creating a duplicate of an object, such that the original and the copied object are separate and distinct. Python offers two types of copying methods known as Deep copy and Shallow copy.

In this course, we will explore both the Deep copy and Shallow copy concept in Python. We will start with the shallow copy, then deep dive into the deep copy and their differences.

Prerequisites:

Before starting this course, you should have the following:

1. A basic knowledge of Python programming language.
2. Python version 3.10 or later installed on your system.

What is a Shallow Copy?

Shallow copy is a process of creating a new object that stores a reference to the original object's memory location. In other words, a shallow copy doesn't create a new object with new memory allocation. Instead, it creates a reference to the original object. A shallow copy creates a new object with memory allocation for itself, but it stores the reference to the original object data.

To implement a shallow copy in Python, you can use the copy() method.

Example code:

```
# Create a list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using the copy() method to create a shallow copy
shallow_copy = original_list.copy()

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)

# Modify the shallow copy
shallow_copy[2][1] = 'shallow'

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
```

Output:

```
Original List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Shallow Copy: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Original List: [[1, 2, 3], [4, 5, 6], [7, 'shallow', 9]]
Shallow Copy: [[1, 2, 3], [4, 5, 6], [7, 'shallow', 9]]
```

In the above example, we have created a list "original_list" that contains three sublists. Then we have created a shallow copy of this original list using the copy() method. After that, we have modified one of the items of the shallow copy. As a result, the changes are reflected in both the original list and the shallow copy. This happens because the shallow copy only stores a reference to the memory location of the original list.

What is a Deep Copy?

A deep copy is a process of creating a new object and assigning it a new memory allocation for the copied data. In other words, a deep copy creates a new object with new memory allocation, and it copies the original object's data to it. Unlike the shallow copy, a deep copy creates an independent copy of the original object. If you change the copied data, it won't affect the original data.

To implement a deep copy in Python, you can use the deepcopy() method.

Example code:

```
import copy

# Create a list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using the deepcopy() method to create a deep copy
deep_copy = copy.deepcopy(original_list)

print("Original List:", original_list)
print("Deep Copy:", deep_copy)

# Modify the deep copy
deep_copy[2][1] = 'deep'

print("Original List:", original_list)
print("Deep Copy:", deep_copy)
```

Output:

```
Original List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Deep Copy: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Original List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Deep Copy: [[1, 2, 3], [4, 5, 6], [7, 'deep', 9]]
```

In the above example, we have created a list "original_list" that contains three sublists. Then we have created a deep copy of this original list using the deepcopy() method. After that, we have modified one of the items of the deep copy. As a result, the changes are NOT reflected in the original list because the deep copy creates a new object with new memory allocation and copies the original data to it.

Conclusion:

Deep copying and shallow copying are the two types of copying methods in Python. Shallow copy creates a new object that stores a reference to the original data's memory location. On the other hand, a deep copy creates a new object and assigns it a new memory allocation for the copied data. You can use the copy() and deepcopy() methods to perform shallow and deep copying, respectively. Understanding these concepts is important because it helps prevent unwanted changes in data and copies objects without impacting the original object.