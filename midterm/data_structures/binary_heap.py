# Copyright 2020 Edoardo Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from math import floor

class Node:
    """
    Class for a single node in the heap.

    Args:
        value (int): The value of the node

    Attributes:
        value (int): The value of the node
    """
    def __init__(self, value):
        self.value = value

    def parent(self, node: int) -> int:
        """
        Calculate the key of the parent of
        the current node.

        Args:
            node (int): The key of the node

        Returns:
            (int): The key of the parent node
        """
        return floor(node / 2) - 1

    def left(self, node: int):
        """
        Calculate the key of the left child of
        the current node.

        Args:
            node (int): The key of the node

        Returns:
            (int): The key of the left node
        """
        return 2 * node + 1

    def right(self, node: int):
        """
        Calculate the key of the right child of
        the current node.

        Args:
            node (int): The key of the node

        Returns:
            (int): The key of the right node
        """
        return 2 * node + 2

heap = [None] * 10
test_heap = [Node(36), Node(21), Node(11), Node(13), Node(20), Node(8), None, None, None, None, None]

def heap_extract_max(heap: list):
    """
    Remove the highest node (first) from the heap
    and move the last node to that position.

    Args:
        heap (list): The heap on which we need to perform
                     the action
    """
    top: int
    size = heap_size(heap)

    if size != 0:
        for index, value in enumerate(heap):
            if value is None:
                top = index - 1
                break

        heap[0], heap[top] = heap[top], None
    else:
        print('Heap Underflow')


def max_heapify(heap: list):
    """
    Chech if which node between the left and right
    nodes of a parent node is bigger. Then swap the
    parent node with the biggest. The action is
    repeated until an empty node is hit.

    Args:
        heap (list): The heap on which we need to perform
                     the action
    """
    for i in range(0, len(heap)):
        if i is not None:
            if heap[heap[i].left(i)] is None or heap[heap[i].right(i)] is None:
                break
            elif heap[heap[i].left(i)].value > heap[heap[i].right(i)].value:
                heap[heap[i].left(i)], heap[i] = heap[i], heap[heap[i].left(i)]
            elif heap[heap[i].right(i)].value > heap[heap[i].left(i)].value:
                heap[heap[i].right(i)], heap[i] = heap[i], heap[heap[i].right(i)]


def build_max_heap(heap: list):
    """
    Apply max_heapify for all elements of the heap from the
    middle (excluding empty Nodes) to the first.

    Args:
        heap (list): The heap on which we need to perform
                     the action
    """
    half = floor(heap_size(heap) / 2)

    for _ in heap[half::-1]:
        max_heapify(heap)


def insert(heap: list, numb: int):
    """
    Add the new Node at the end of the heap (i.e. immediately
    before the first empty node) and bild a max_heap.

    Args:
        heap (list): The heap on which we need to perform
                     the action
        numb (int): The value of the node to insert
    """
    size = heap_size(heap)

    if size < len(heap):
        heap[size] = Node(numb)
        build_max_heap(heap)
    else:
        print('Heap Overflow')


def heap_size(heap: list) -> int:
    """
    Calculate the actual size of a heap, without all the
    empty nodes.

    Args:
        heap (list): The heap on which we need to perform
                     the action

    Returns:
        (int): The actual size of the heap
    """
    elements = 0

    for i in test_heap:
        if i is not None:
            elements += 1

    return elements


def print_heap(heap: list) -> str:
    """
    Print an array containing all the values of the nodes
    in the heap plus the actual size of the heap.

    Args:
        heap (list): The heap on which we need to perform
                     the action

    Returns:
        (str): The heap and the size of the heap
    """
    printable = []

    for i in test_heap:
        if i is not None:
            printable.append(i.value)
        else:
            printable.append(None)

    return '{} {}\n%'.format(printable, heap_size(test_heap))


# Driver
for l in sys.stdin:
    l = l.split()

    if len(l) == 0:
        print('%')
        continue

    elif l[0] == 'build':
        build_max_heap(test_heap)
        print('%')

    elif l[0] == 'insert':
        if l[1] != '':
            insert(test_heap, int(l[1]))
        else:
            print('You must add an argument')
        print('%')

    elif l[0] == 'extract_max':
        heap_extract_max(test_heap)
        print('%')

    elif l[0] == 'heapify':
        max_heapify(test_heap)
        print('%')

    elif l[0] == 'print':
        print(print_heap(test_heap))

    else:
        print('unknown command:', l[0])
        print('%')
