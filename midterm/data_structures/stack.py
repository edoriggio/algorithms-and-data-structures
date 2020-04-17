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

class Stack:
    """
    This class represents a stack. A stack is a LIFO data
    structure (Last In First Out) of fixed size. When
    initialized, it creates a stack of a number of None
    objects equal to the length that is given as parameter.

    Args:
        length (int): The length of the stack

    Attributes:
        length (int): The length of the stack
        top (int): The index of the last element of the stack
        is_empty (bool): Indicates if the stack is empty or not
        data (list): The data contained in the stack
    """
    def __init__ (self, length: int):
        self.length = length
        self.data = [None] * self.length
        self.top = 0
        self.is_empty = True

    def push(self, element: int):
        """
        Add the element passed as input at the end of the stack.
        This element must be added iff the stack is not full yet
        (i.e. top is smaller than the length of the stack).

        Args:
            element (int): The element to be added to the stack
        """
        if self.top < self.length:
            self.data[self.top] = element
            self.top += 1
            self.is_empty = False
        else:
            print('Stack Overflow')

    def pop(self):
        """
        Remove the last element of the stack and print it in the
        terminal. The element must be removed iff the stack is not
        empty yet (i.e. top is not equal to 0).
        """
        if self.top != 0:
            print(self.data[self.top-1])
            self.top -= 1
            self.data[self.top] = None
            self.is_empty = True if self.top == 0 else False
        else:
            self.is_empty = True
            print('Stack Underflow')
    
    def check_empty(self) -> bool:
        """
        Check if the stack is empty or not.

        Returns:
            (bool): True if the stack is empty
                    False otherwise
        """
        print(self.is_empty)

    def print_self(self):
        """
        Print the data, top and is_empty values of the stack.
        """
        print('data: {}\ntop: {}\nEmpty: {}'.format(self.data, self.top, self.is_empty))

test_stack: Stack

# Driver
for l in sys.stdin:
    l = l.split()

    if len(l) == 0:
        print('%')
        continue

    if l[0] == 'init':
        test_stack = Stack(int(l[1]))
        print('%')

    if l[0] == 'push':
        test_stack.push(int(l[1]))
        print('%')

    elif l[0] == 'pop':
        test_stack.pop()
        print('%')

    elif l[0] == 'empty':
        test_stack.check_empty()
        print('%')

    elif l[0] == 'print':
        test_stack.print_self()
        print('%')

    else:
        print('unknown command:', l[0])
        print('%')
