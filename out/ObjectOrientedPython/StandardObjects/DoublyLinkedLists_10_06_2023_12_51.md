
doubly linked lists
===================
Introduction
Doubly linked lists are a type of data structure in which each node holds a reference to both its previous and next node, effectively creating a linked list that can be traversed in both directions. This makes it useful for certain types of tasks, such as when you need to access the previous node or add elements to the beginning of the list. In this course, we will be going over how to create and manipulate doubly linked lists in Python version 3.10.

Prerequisites
Before we start, you should have a basic understanding of Python programming concepts such as variables, functions, loops, and classes. You should also be familiar with linked lists and how they are structured.

Creating a Doubly Linked List
Let's start by creating a simple doubly linked list. First, we need to create a class for our nodes. Each node will have three attributes - a value, a reference to the next node, and a reference to the previous node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

To create a doubly linked list, we first need to define its head (the first node in the list). We will also add a tail attribute to make it easier to insert new elements to the end of the list.

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

Now, let's add a method to add a node to the list. This method will take a value as an argument and create a new node with that value, then add it to the end of the list.

def insert(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

This method first creates a new node with the value passed in. If the head is None (meaning the list is empty), it sets both the head and the tail to the new node. Otherwise, it sets the previous attribute of the new node to the current tail, sets the next attribute of the current tail to the new node, and updates the tail to the new node.

Now, let's add a method to print the contents of the list.

def print_list(self):
    if self.head is None:
        print("List is empty")
    else:
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

This method simply checks if the head is None (meaning the list is empty), and if not, it iterates through the list and prints out each node's value.

Inserting and Deleting Nodes
Now that we have our basic doubly linked list structure set up, let's look at how to insert and delete nodes.

To insert a node at a specific position in the list, we need to first traverse the list to find the node with the position we want to insert at. We can do this using a for loop and a counter variable.

def insert_at_pos(self, value, pos):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    elif pos == 1:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    else:
        current = self.head
        counter = 1
        while counter < pos and current is not None:
            current = current.next
            counter += 1
        if current is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.prev = current.prev
            current.prev.next = new_node
            new_node.next = current
            current.prev = new_node

This method first creates a new node with the passed-in value. If the list is empty, it sets both the head and tail to the new node. If pos is 1 (meaning we want to insert at the beginning of the list), it sets the next attribute of the new node to the current head, the previous attribute of the current head to the new node, and updates the head to the new node. Otherwise, it iterates through the list using a counter variable. If the current node is None (meaning we've reached the end of the list), it sets the next attribute of the current tail to the new node, the previous attribute of the new node to the current tail, and updates the tail to the new node. Otherwise, it sets the previous attribute of the new node to the previous node of the current node, sets the next attribute of the previous node of the current node to the new node, sets the next attribute of the new node to the current node, and sets the previous attribute of the current node to the new node.

To delete a node at a specific position in the list, we also need to traverse the list to find the node with the position we want to delete at. We can do this using a for loop and a counter variable, similar to inserting a node at a specific position.

def delete_at_pos(self, pos):
    if self.head is None:
        print("List is empty")
    elif pos == 1:
        self.head = self.head.next
        self.head.prev = None
    else:
        current = self.head
        counter = 1
        while counter < pos and current is not None:
            current = current.next
            counter += 1
        if current is None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

This method first checks if the list is empty. If it is, it prints out a message saying so. If pos is 1 (meaning we want to delete the first node), it sets the head to the next node, sets the previous attribute of the new head to None, and effectively deletes the old head node. Otherwise, it iterates through the list using a counter variable. If the current node is None (meaning we've reached the end of the list without finding the position), it sets the tail to the previous node of the current node, sets its next attribute to None, and effectively deletes the current node. Otherwise, it sets the next attribute of the previous node of the current node to the next node, sets the previous attribute of the next node to the previous node of the current node, and effectively deletes the current node.

Conclusion
That's it! You now know how to create and manipulate doubly linked lists in Python version 3.10. The key concept to remember is that each node has a reference to both its previous and next node, which allows us to traverse the list in both directions. Keep practicing, and you'll have a strong foundation for working with more complex data structures.