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
# Best case -> Θ(n)
# Average case -> Θ(n^2)
# Worst case -> Θ(n^2) -> When the list is in reversed order


def insertion_sort(array: list) -> list:
    """
    Go through the array from left to right. If the number in
    the i-th position is smaller than the number before it,
    swap the two elements. Repeat the same procedure until
    the array is sorted (i.e. when the end of the array is
    reached).

    :param array: The array to be sorted
    :return: The sorted array
    """

    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1

        array[i+1] = key

    return array


if __name__ == '__main__':
    data = [int(i) for i in input().split(" ")]
    print(insertion_sort(data))
