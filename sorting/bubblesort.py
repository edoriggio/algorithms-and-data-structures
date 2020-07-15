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
# Best case -> O(n) -> When the array is already sorted
# Average case -> O(n^2)
# Worst case -> O(n^2)


def bubblesort(numbs: list) -> list:
    """
    Go through the array from left to right, for each couple of
    numbers, check which one is bigger. If the first element of
    the couple is bigger than the second, swap the two numbers.
    Repeat the same process until the array is sorted (i.e.
    when the number of swaps is equal to 0).

    :param numbs: The array to be sorted
    :return: The sorted array
    """
    for i in range(len(numbs) - 1):
        for j in range(len(numbs) - i - 1):
            if numbs[j] > numbs[j + 1]:
                numbs[j], numbs[j + 1] = numbs[j + 1], numbs[j]

    return numbs


if __name__ == '__main__':
    data = [int(i) for i in input().split(" ")]
    print(bubblesort(data))
