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

import sys

class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert_element(self, value):
        current = self.root
        parent = None
        while current != None:
            parent = current
            if value > current.key:
                current = current.right
            else:
                current = current.left

        if parent is None:
            self.root = Node(value)
        elif value > parent.key:
            parent.right = Node(value)
        else:
            parent.left = Node(value)

    def insert(self, xs):
        if isinstance(xs, (list, tuple)):
            for x in xs:
                self.insert_element(x)
        else:
            self.insert_element(xs)

    def max(self):
        parent = None
        current = self.root
        while current != None:
            parent = current
            current = current.right
        return parent

    def max_key(self):
        return self.max().key

    def min(self):
        parent = None
        current = self.root
        while current != None:
            parent = current
            current = current.left
        return parent

    def min_key(self):
        return self.min().key

    def find(self, value):
        current = self.root
        while current != None:
            if current.key == value:
                return current
            if value > current.key:
                current = current.right
            else:
                current = current.left
        return None

    def print_in_order(self, root):
        if root != None:
            self.print_in_order(root.left)
            print(root.key," ",end='')
            self.print_in_order(root.right)

    def print(self):
        self.print_in_order(self.root)
        print("")

test_tree: BST

# Driver
for l in sys.stdin:
    l = l.split()

    if len(l) == 0:
        print('%')
        continue

    elif l[0] == 'init':
        test_tree = BST()
        print('%')

    elif l[0] == 'insert':
        print('%')

    elif l[0] == 'in_order_walk':
        print('%')

    elif l[0] == 'pre_order_walk':
        print('%')

    elif l[0] == 'post_order_walk':
        print('%')

    elif l[0] == 'reverse_walk':
        print('%')

    elif l[0] == 'minimum':
        print('%')

    elif l[0] == 'maximum':
        print('%')

    elif l[0] == 'predecessor':
        print('%')

    elif l[0] == 'successor':
        print('%')

    elif l[0] == 'search':
        print('%')

    else:
        print('unknown command:', l[0])
        print('%')
