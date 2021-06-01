# Copyright 2021 Edoardo Riggio
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

class Heap:
    """ Class for the Binary Heap data structure. It contains data and
    metadata, as well as functions, of the data structure.
    """
    heap: list

    def __init__(self):
        self.heap = []

    def parent(self, element):
        """Calculate the parent of the given element.

        Args:
            element (int): the element to calculate the parent of

        Returns:
            int: the parent of the given element
        """
        return (element - 1) // 2

    def left_child(self, element):
        """Calculate the left child of the given element.

        Args:
            element (int): the element to calculate the left child of

        Returns:
            int: the left child of the given element
        """
        return element * 2 + 1

    def right_child(self, element):
        """Calculate the right child of the given element.

        Args:
            element (int): the element to calculate the right child of

        Returns:
            int: the right child of the given element
        """
        return element * 2 + 2


def max_heapify(arr):
    """Transform the given array into a binary max-heap.

    Args:
        arr (list): the array to transform

    Returns:
        Heap: the transformed heap
    """
    heap = Heap
    heap.heap = arr

    for i in range(len(heap.heap)):
        max_reorder(heap, 0, i)

    return heap


def max_reorder(heap, begin, end):
    """A recursive helper function that reorders the array in order
    to obtain a binary max-heap

    Args:
        heap (Heap): the unordered heap to be transformed
        begin (int): the beginning of the subarray
        end (int): the end of the subarray
    """
    if end == begin or end == 0:
        return

    if heap.heap[heap.parent(heap, end)] < heap.heap[end]:
        heap.heap[heap.parent(heap, end)], heap.heap[end] = \
            heap.heap[end], heap.heap[heap.parent(heap, end)]

        max_reorder(heap, begin, heap.parent(heap, end))

    return
