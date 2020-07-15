# Sorting Algorithms

## Insertion Sort

### Abstract

Insertion sort is an efficient algorithm when we have a small array to sort. We start at the left-hand side of the
array, and check if the number is smaller than the number before it. At any time, we will have the left-hand side of
the array to be sorted. Below is the pseudocode representation of the algorithm.

### Design

Incremental

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

The merge sort algorithm takes advantage of the divide-and-conquer-approach. The initial array is divided in half
recursively. The subarrays are sorted recursively using merge sort. Finally the two subarrays (i.e. the two halves)
are merged together.

### Design

Divide-and-Conquer

### Complexity

- **Best Case** - Θ(n log(n))
- **Average Case** - Θ(n log(n))
- **Worst Case** - Θ(n log(n))

### Execution Times - [[script](/plots/merge_sort_plot.py)]

<p align="center">
  <img src="/plots/assets/merge_sort.png" alt="merge sort">
</p>
