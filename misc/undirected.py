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

import sys


def read_undirected():
    """Read undirected graphs from input.

    Returns:
        dict: set of nodes and their connections
    """
    Nodes = {}

    for line in sys.stdin:
        regions = line.split()

        for i in range(len(regions)):
            try:
                Nodes[regions[i]]
            except KeyError:
                Nodes[regions[i]] = []

        for i in range(1, len(regions)):
            Nodes[regions[i]].append(regions[0])
            Nodes[regions[0]].append(regions[i])

    return Nodes
