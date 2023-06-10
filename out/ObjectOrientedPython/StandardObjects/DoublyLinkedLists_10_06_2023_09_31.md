
doubly linked lists
===================
Introduction:

Doubly linked list is a type of data structure in which each node contains a reference to the previous and the next node in the sequence. It can be used to implement various operations such as insertion, deletion, searching, and sorting. In this course, we will learn how to implement a doubly linked list in Python 3.10.

Prerequisites:

Before starting this course, you should have a basic understanding of Python programming language. You should know about the basics of linked lists and basic data structures in Python like lists, sets, and dictionaries.

Step 1: Creating a Node Class

The first step in creating a doubly linked list is to create a node class that will hold the data and pointers to the previous and next nodes. We will create a Node class and define its __init__ function to initialize the data, prev, and next pointers:

```
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

In this code, we define a Node class that has three attributes: data, prev, and next. The data attribute holds the actual data of the node, and the prev and next attributes hold references to the previous and next nodes in the sequence. 

Step 2: Creating a DoublyLinkedList Class

The next step is to create a DoublyLinkedList class that will define a set of methods to manipulate the linked list. We will create a class with __init__ function to initialize the head and tail pointers:

```
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

In this code, we define a DoublyLinkedList class that has two attributes: head and tail. The head attribute holds a reference to the first node in the sequence, and the tail attribute holds a reference to the last node in the sequence.

Step 3: Adding Elements to the List

The next step is to add elements to the list. We will create an add_node function that takes a data parameter and adds a new node to the end of the list:

```
def add_node(self, data):
    new_node = Node(data)
    
    if self.head is None:
        # If the list is empty, make the new node the head and tail of the list
        self.head = new_node
        self.tail = new_node
    else:
        # Otherwise, add the new node to the end of the list
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
```
In this code, we first create a new node with the given data. If the list is empty, we set the head and the tail pointers to the new node. Otherwise, we set the prev pointer of the new node to the current tail and the next pointer of the current tail to the new node. We then update the tail pointer to point to the new node.

Step 4: Removing Elements from the List

The next step is to remove elements from the list. We will create a remove_node function that takes a data parameter and removes the first occurrence of the node containing that data:

```
def remove_node(self, data):
    current_node = self.head
    
    while current_node is not None:
        if current_node.data == data:
            # If this is the first node, update the head pointer
            if current_node.prev is None:
                self.head = current_node.next
                current_node.next.prev = None
            # If this is the last node, update the tail pointer
            elif current_node.next is None:
                self.tail = current_node.prev
                current_node.prev.next = None
            # Otherwise, update the pointers of the surrounding nodes
            else:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
            return True
        
        current_node = current_node.next
        
    return False
```

In this code, we first set the current_node pointer to the head of the list. We then traverse the list until we find a node containing the given data. If we find the node, we update the pointers of the surrounding nodes to remove the node from the list. If the node is the first or last node in the list, we update the head or tail pointers, respectively. If the node is in the middle of the list, we update the next and prev pointers of the surrounding nodes. If we cannot find the node, we return False.

Step 5: Traversing the List

The next step is to traverse the list. We will create a traverse function that will loop through the list and print the data of each node:

```
def traverse(self):
    current_node = self.head
    
    while current_node is not None:
        print(current_node.data, end=' ')
        current_node = current_node.next
        
    print()
```

In this code, we first set the current_node pointer to the head of the list. We then loop through the list and print the data of each node. We update the current_node pointer to the next node until we reach the end of the list.

Step 6: Implementing Other Operations

Other operations that can be implemented on a doubly linked list include inserting a node at a specific position, getting the size of the list, and reversing the list. 

Inserting a node at a specific position:

```
def insert_node(self, data, pos):
    new_node = Node(data)
    current_node = self.head
    count = 0
    
    if pos == 0:
        # If the node is to be inserted at the beginning of the list
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return True
    else:
        # Otherwise, traverse the list until we reach the insertion point
        while current_node is not None:
            if count == pos:
                new_node.prev = current_node.prev
                new_node.next = current_node
                current_node.prev.next = new_node
                current_node.prev = new_node
                return True
            
            count += 1
            current_node = current_node.next
            
    return False
```

Getting the size of the list:

```
def size(self):
    current_node = self.head
    count = 0
    
    while current_node is not None:
        count += 1
        current_node = current_node.next
        
    return count
```

Reversing the list:

```
def reverse(self):
    current_node = self.head
    temp = None
    
    while current_node is not None:
        temp = current_node.prev
        current_node.prev = current_node.next
        current_node.next = temp
        current_node = current_node.prev
        
    if temp is not None:
        self.head = temp.prev
```

Conclusion:

In this course, we learned how to implement a doubly linked list in Python 3.10. We created a Node class and a DoublyLinkedList class to store the nodes and provide a set of methods for manipulating the list. We implemented operations such as adding and removing nodes, traversing the list, inserting a node at a specific position, getting the size of the list, and reversing the list. With this knowledge, you can now apply doubly linked lists to a wide variety of real-world applications.