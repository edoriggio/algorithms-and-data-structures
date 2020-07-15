# Sorting Algorithms

A sorting algorithm is an algorithm that is used to put the elements of an array in a certain order.

## Bubblesort

### Abstract

This simple algorithm performs poorly in real world use and is used primarily as an educational tool. It works by
repeatedly swapping adjacent elements that are out of order.

### Design

- Incremental
- For educational purposes

### Complexity

- **Best Case** - O(n^2)
- **Average Case** - O(n^2)
- **Worst Case** - O(n^2)

### Execution Times - [[script](/plots/bubblesort_plot.py)]

<p align="center">
  <img src="/plots/assets/bubblesort.png" alt="insertion sort">
</p>

## Insertion Sort

### Abstract

Insertion sort is an efficient algorithm when we have a small array to sort. We start at the left-hand side of the
array, and check if the number is smaller than the number before it. At any time, we will have the left-hand side of
the array to be sorted. Below is the pseudocode representation of the algorithm.

### Design

- Incremental
- For small arrays

### Complexity

- **Best Case** - Θ(n)
- **Average Case** - Θ(n^2)
- **Worst Case** - Θ(n^2)

### Execution Times - [[script](/plots/insertion_sort_plot.py)]

<p align="center">
  <img src="/plots/assets/insertion_sort.png" alt="insertion sort">
</p>

## Merge Sort

### Abstract

The merge sort algorithm takes advantage of the divide-and-conquer approach. The initial array is divided in half
recursively. The subarrays are sorted recursively using merge sort. Finally the two subarrays (i.e. the two halves)
are merged together.

### Design

- Divide-and-Conquer
- For large arrays

### Complexity

- **Best Case** - O(n log(n))
- **Average Case** - O(n log(n))
- **Worst Case** - O(n log(n))

### Execution Times - [[script](/plots/merge_sort_plot.py)]

<p align="center">
  <img src="/plots/assets/merge_sort.png" alt="merge sort">
</p>

> In all execution times graphs, arrays with elements from 1 to 10.000 are sorted with a step of 50
> in between them (i.e. every time the elements in the array are increased by 50)
