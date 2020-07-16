import sys
from math import floor

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
