# Sorting Algorithms

A sorting algorithm is an algorithm that is used to put the elements of an array in a certain order.

## Bubblesort

### Abstract

This simple algorithm performs poorly in real world use and is used primarily as an educational tool. It works by repeatedly swapping adjacent elements that are out of order. This is done until the array is sorted.

### Design

- Incremental
- In-place
- For educational purposes

### Complexity

- **Best Case** - Θ(n^2)
- **Average Case** - Θ(n^2)
- **Worst Case** - Θ(n^2)

### Execution Times - [[script](/plots/bubblesort_plot.py)]

<!--suppress ALL-->
<p align="center">
  <img src="/plots/assets/bubblesort.png" alt="bubblesort">
</p>

## Insertion Sort

### Abstract

Insertion sort is an efficient algorithm when we have a small array to sort. We start at the left-hand side of the array, and check if the number is smaller than the number before it. At any time, we will have the left-hand side of the array to be sorted. Below is the pseudocode representation of the algorithm.

### Design

- Incremental
- In-place
- For small arrays

### Complexity

- **Best Case** - Θ(n)
- **Average Case** - Θ(n^2)
- **Worst Case** - Θ(n^2)

### Execution Times - [[script](/plots/insertion_sort_plot.py)]

<p align="center">
  <img src="/plots/assets/insertion_sort.png" alt="insertion sort">
</p>

## Selection Sort

### Abstract

The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest element in the unsorted sublist, swapping it with the leftmost unsorted element, and moving the sublist boundaries one element to the right.

### Design

- Incremental
- In-place
- For small arrays

### Complexity

- **Best Case** - Θ(n^2)
- **Average Case** - Θ(n^2)
- **Worst Case** - Θ(n^2)

### Execution Times - [[script](/plots/selection_sort_plot.py)]

<p align="center">
  <img src="/plots/assets/selection_sort.png" alt="selection sort">
</p>

## Quick Sort

### Abstract

Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This can be done in-place.

### Design

- Recursive
- In-place
- Efficient

### Complexity

- **Best Case** - Θ(n log(n))
- **Average Case** - Θ(n log(n))
- **Worst Case** - Θ(n^2)

### Execution Times - [[script](/plots/quick_sort_plot.py)]

<p align="center">
  <img src="/plots/assets/quick_sort.png" alt="quick sort">
</p>

## Merge Sort

### Abstract

The merge sort algorithm takes advantage of the divide-and-conquer approach. The initial array is divided in half recursively. The subarrays are sorted recursively using merge sort. Finally the two subarrays (i.e. the two halves) are merged together.

### Design

- Recursive
- For large arrays
- Efficient

### Complexity

- **Best Case** - Θ(n log(n))
- **Average Case** - Θ(n log(n))
- **Worst Case** - Θ(n log(n))

### Execution Times - [[script](/plots/merge_sort_plot.py)]

<p align="center">
  <img src="/plots/assets/merge_sort.png" alt="merge sort">
</p>

## Hepsort

### Abstract

Heapsort divides the input into a sorted and an unsorted region. It then takes the largest element from the unsorted region and inserts it into the sorted region. The unsorted region is kept as a heap, which allows finding the largest element quickly.

### Design

- For large arrays
- In-place
- Efficient

### Complexity

- **Best Case** - Θ(n log(n))
- **Average Case** - Θ(n log(n))
- **Worst Case** - Θ(n log(n))

### Execution Times - [[script](/plots/heapsort_plot.py)]

<p align="center">
  <img src="/plots/assets/heapsort.png" alt="heapsort">
</p>

> In all execution times graphs, arrays from 1 element to 10.000 elements are sorted with a step of 50 in between them
> (i.e. every time the elements in the array are increased by 50)

> Machine used to calculate results: MacBook Pro 2019, 2.6 GHz 6-Core Intel Core i7, 16 GB 2400 MHz DDR4
