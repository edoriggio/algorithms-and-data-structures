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

# Time complexity -> O(|V|+|E|)

from graphs import *

def bfs_algo(graph, start, print_out = True):
    """
    Function that recreates the Breath First Search
    algorithm, using a queue as its data structure.
    In this algorithm, when a node is analyzed, it is
    marked as visited and all of its children are
    added to the queue (if their not in it already).
    The next node to be analyzed is given both by the
    queue and the 'visited' array. If a node is
    dequeued and it is not in the 'visited' array, then
    it is analyzed.

    Args:
        graph (dict): A dictionary representing the graph
                      to analyze
        start (Any): Where to start the analysis
        print_out (Bool, default: True): Decide whether to
                                         print the steps

    Returns:
        (list): An array containing the nodes in the order
                of how they were visited
    """
    visited = []
    if start in graph:
        stack = [start]
    else:
        stack = []

    while queue:
        element = queue.pop(0)
        
        for neighbor in graph[element]:
            if neighbor not in queue:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        if element not in visited:
            visited.append(element)

        if print_out:
            print('Node:', element,\
                '  Queue:', queue,\
                '  Visited:', visited)
    
    return visited

print(bfs_algo(graph_numbers, 1), end='\n\n')
print(bfs_algo(graph_letters, 'A', False), end='\n\n')
