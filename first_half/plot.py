# Time complexities:
# Best case -> O(n) -> When the list is already sorted
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

import matplotlib.pyplot as plt


def plot_times(times_array, name):
    times = [i[0] for i in times_array]
    elements = [i[1] for i in times_array]

    plt.plot(elements, times)
    plt.xlabel('Elements')
    plt.ylabel('Time (s)')
    plt.xlim(0, elements[-1]+10)
    plt.ylim(0, max(times)+0.005)
    plt.isinteractive()
    plt.title(name)
    plt.show()
