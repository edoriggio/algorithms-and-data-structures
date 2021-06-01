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

class Node:
    """Class containing the metadata of a BST node, namely the value of 
    the node, its right child, and its left child.
    """

    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


def bst_insert(t, n):
    """Insert the given node inside of the given BST.

    Args:
        t (Node): the BST
        n (Node): the node

    Returns:
        Node: the given BST with the new node inserted
    """
    if t is not None:
        if n.key < t.key:
            t.left = bst_insert(t.left, n)
        else:
            t.right = bst_insert(t.right, n)
    else:
        t = n
    return t
