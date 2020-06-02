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

graph_numbers = {
    1: [5,6],
    2: [3,7],
    3: [4,7],
    4: [7],
    5: [9],
    6: [2,7,9],
    7: [8,10,11],
    8: [11,12],
    9: [10],
    10: [],
    11: [12],
    12: []
}

graph_letters = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

graph_dijkstra = {
    'a' : {'b': 3, 'e': 1, 'd': 1},
    'b' : {'c': 4, 'f': 2, 'e': 1, 'a': 3},
    'c' : {'b': 4, 'f': 2},
    'd' : {'e': 3, 'a': 1, 'g': 1},
    'e' : {'d': 3, 'f': 9, 'b': 1, 'h': 1},
    'f' : {'j': 2, 'h': 4, 'e': 9, 'b': 2, 'c': 1},
    'g' : {'d': 1},
    'h' : {'j': 1, 'f': 4, 'e': 1},
    'j' : {'h': 1, 'f': 2}
}
