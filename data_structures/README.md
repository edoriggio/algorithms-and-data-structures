# Data Structures Algorithms

A data structure is a way to organize and store information. These data structures store data and possibly metadata

## Stack

### Abstract

It is a data structure that serves as a collection of elements, with two main operations:

- **Push** - adds an element to the collection
- **Pop** - removes the most recently added element that was not yet removed

The elements of this data structure are taken and added using a **LIFO** (Last-In First-Out) order. Elements can only be added on the top of the stack and are then removed from the top.

### Complexities

- **Push** - Θ(1)
- **Pop** - Θ(1)

## Queue

### Abstract

It is a data structure with fixed size of length *n*, with two main operations:

- **Enqueue** - adds an element to the collection
- **Dequeue** - removes the first element from the collection that was not yet removed

The elements of these data structure are taken and added wsing a **FIFO** (First-In First-Out) order. Elements can only be added at the beginning of the queue and taken from the end of the queue.

### Complexities

- **Enqueue** - Θ(1)
- **Dequeue** - Θ(1)

## Binary Heap

### Abstract

It is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property. There are two types of binary heaps:

- **Max Heap** - every parent node is greater than or equal to its children
- **Min Heap** - every parent node is less than or equal to its children

### Complexities

- **Heapify** - O(log(n))
- **Extract Min/Max** - O(log(n))
- **Get Min/Max** - Θ(1)

## Binary Search Tree

### Abstract

A binary search tree is a rooted binary tree whose internal nodes each store a key greater than all the keys in the node's left subtree and less than those in its right subtree.

### Complexities

- **Insert Node** - O(log(n))
- **Delete Node** - O(log(n))
