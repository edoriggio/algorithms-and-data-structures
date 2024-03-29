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
# Best case -> O(n log(n))
# Average case -> O(n log(n))
# Worst case -> O(n^2)


def partition(array: list, beginning: int, end: int) -> int:
    """
    Go through the array from left to right. If the number in
    position i is bigger than the pivot (i.e. the last number
    of the array) and the number in position j is smaller than
    or equal to the pivot, then swap the two numbers and increase
    i by one. When the end is reached, then swap the number
    in position i + 1 with the pivot and make i + 1 the pivot.

    :param array: The array that needs to be partitioned
    :param beginning: The beginning index of the array
    :param end: The ending index of the array
    :return: The partitioned array
    """
    pointer = beginning - 1
    pivot = array[end]

    for i in range(beginning, end):
        if array[i] <= pivot:
            pointer += 1
            array[pointer], array[i] = array[i], array[pointer]

    array[end], array[pointer + 1] = array[pointer + 1], array[end]
    pivot = pointer + 1

    return pivot


def quick_sort(array: list, beginning: int, end: int):
    """
    If the index low is less than the index high, then
    partition the array. The process is repeated for the
    right part of the array (i.e. numbs[pi+1:]) and the
    left part of the array (i.e. numbs[:pi-1]). The
    algorithm will stop when the array is sorted.

    :param array: The array to be sorted
    :param beginning: The beginning index of the array
    :param end: The ending index of the array
    :return: The sorted array
    """
    if beginning < end:
        mid = partition(array, beginning, end)
        quick_sort(array, beginning, mid-1)
        quick_sort(array, mid+1, end)

    return array


if __name__ == '__main__':
    data = [int(i) for i in input().split(" ")]
    print(quick_sort(data, 0, len(data)-1))
