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

# Time complexities:
# Best case -> O(nlog(n))
# Average case -> O(nlog(n))
# Worst case -> O(nlog(n))

from math import floor


def heapsort(heap):
    """
    Build a max-heap from the array given as input, and then
    iterate from the end of the heap to the beginning. During
    this iteration swap the node in the i-th position with the
    first node. Now the property of the max-heap is not respected,
    thus we need to max_heapify the heap in order to restablish
    the property.

    Args:
        heap (list): The heap to be sorted

    Returns:
        (list): The sorted heap
    """
    build_max_heap(heap)
    i = len(heap) - 1
    heap_size = len(heap)

    while i >= 1:
        temp = heap[0]
        heap[0] = heap[i]
        heap[i] = temp
        heap_size -= 1
        max_heapify(heap, 0, heap_size)
        i -= 1

    return heap


# Heap aux functions

def parent(i):
    return floor(i / 2)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    i = int((floor(len(A))) / 2)
    while i >= 0:
        max_heapify(A, i, len(A))
        i -= 1
