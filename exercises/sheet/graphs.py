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

graph_no_cycles = {
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

graph_letters_cycle_4 = {
    'A' : ['B'],
    'B' : ['D', 'E'],
    'C' : ['A'],
    'D' : [],
    'E' : ['C'],
    'F' : []
}

graph_letters_cycle = {
    'A' : ['B'],
    'B' : ['D', 'E'],
    'C' : ['A'],
    'D' : [],
    'E' : ['F'],
    'F' : ['C']
}

user_network = {
    'a' : ['h', 'f'],
    'b' : ['g','i','e'],
    'c' : ['i','f','e'],
    'd' : ['i', 'e']
}