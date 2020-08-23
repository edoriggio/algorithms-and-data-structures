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

import random
import time

import tqdm

import plots.plot
from sorting.quick_sort import quick_sort


def running_times(n_tests, steps):
    """
    Go though the tests until the number of elements is equal
    to the one given by the user. Creates an array of tuples
    composed by the execution time and the number of elements
    that where sorted.

    :param n_tests: The number of elements to be executed
    :param steps: The number of tests to skip every iteration
    :return: The array of times and number of elements
    """
    times = []

    for i in tqdm.tqdm(range(0, n_tests, steps)):
        start_t = time.time()
        input_data = [random.randint(0, 200) for _ in range(i)]
        quick_sort(input_data, 0, len(input_data)-1)
        end_t = time.time()

        times.append((end_t - start_t, i))

    return times


if __name__ == '__main__':
    data = running_times(int(input("Max Elements: \n >> ")),
                         int(input("Step: \n >> ")))
    plots.plot.plot_times(data, 'Selection Sort')
