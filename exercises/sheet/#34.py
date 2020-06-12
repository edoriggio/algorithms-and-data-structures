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

# Problem:
# If A is a min-heap, then extract the minimum value and then rearrange
# the array with the min-heapify procedure.

def min_heapify(A, i, le):
    if(i == 0):
        l = 1
        r = 2
    else:
        l = (i * 2) - 1
        r = i * 2

    if (l < le and A[l] < A[i]):
        smallest = l
    else:
        smallest = i
    if(r < le and A[r] < A[smallest]):
        smallest = r
    if(smallest != i):
        temp = A[i]
        A[i] = A[smallest]
        A[smallest] = temp
        return min_heapify(A, smallest, le)

def build_min_heap(A):
    i = len(A) // 2
    while i >= 0:
        min_heapify(A,i,len(A))
        i = i - 1

def min_heap_insert(A, x):
    A.append(x)
    build_min_heap(A)

def heap_extract_min(heap: list):
    result = heap.pop(0)
    build_min_heap(heap)
    return result

heap = []
array = [4,33,6,90,33,32,31,91,90,89,50,33]

for i in array:
    min_heap_insert(heap, i)

print(heap)
print(heap_extract_min(heap))
print(heap)
