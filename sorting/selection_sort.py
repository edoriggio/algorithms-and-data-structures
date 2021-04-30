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
# Best case -> O(n^2)
# Average case -> O(n^2)
# Worst case -> O(n^2)


def selection_sort(numbs: list) -> list:
    """
    Go through the list from left to right and search for the
    minimum. Once the minimum is found, swap it with the
    element at the end of the array. Repeat the same procedure
    on the subarray that goes from the element after 'i' to the
    end, until the array is sorted (i.e. when the subarray is
    composed of only one element).

    :param numbs: The array to be sorted
    :return: The sorted array
    """
    for i in range(len(numbs)):
        minimum = i

        for j in range(i + 1, len(numbs)):
            if numbs[minimum] > numbs[j]:
                minimum = j

        numbs[i], numbs[minimum] = numbs[minimum], numbs[i]

    return numbs


if __name__ == '__main__':
    data = [int(i) for i in input().split(" ")]
    print(selection_sort(data))
