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

# Time complexities:
# Best case -> O(nlog(n))
# Average case -> O(nlog(n))
# Worst case -> O(nlog(n))

from binary_heap import Node, build_max_heap, max_heapify, heap_size

numbs = [Node(int(i)) for i in input().split(' ')]

def heap_sort(heap: list) -> list:
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
    size = heap_size(heap) - 1
    build_max_heap(heap)

    for i in range(size, 1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        size -= 1
        max_heapify(heap, size)

    printable = []

    for i in heap:
        printable.append(i.value)

    return printable

# Test with user input
print(heap_sort(numbs))

# Tests without user input
assert heap_sort([Node(5),Node(2),Node(7),Node(4),Node(1)]) == [1,2,4,5,7]