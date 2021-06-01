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

def bfs(graph):
    """Function that recreates the Breath First Search
    algorithm, using a queue as its data structure.
    In this algorithm, when a node is analyzed, it is
    marked as visited and all of its children are
    added to the queue (if they are not in it already).
    The next node to be analyzed is given both by the
    queue and the 'visited' array. If a node is
    dequeued and it is not in the 'visited' array, then
    it is analyzed. 

    Args:
        graph (dict): a dictionary mapping the nodes of the graph
                      to their connections.

    Returns:
        array: the array of visited nodes in order of visiting
    """
    visited = []

    for key in graph.keys():
        queue = [key]
        head = 0

        if key in visited:
            continue

        while head < len(queue):
            if queue[head] in visited:
                continue

            for i in range(len(graph[queue[head]])):
                if graph[queue[head]][i] not in queue:
                    queue.append(graph[queue[head]][i])

            visited.append(queue[head])
            head += 1

    return visited
