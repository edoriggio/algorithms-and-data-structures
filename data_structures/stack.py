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

class Stack:
    """Class for the Stack data structure. It contains data and metadata
    about the Stack.
    """
    stack: list
    top: int

    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        """Return if the Stack is empty or not.

        Returns:
            Bool: stack is empty or not
        """
        return self.top == -1

    def push(self, value):
        """Push the given value onto the stack.

        Args:
            value (void): the value to push
        """
        self.top += 1
        self.stack.append(value)

    def pop(self):
        """Pop the last value from the stack and return it.

        Returns:
            void: the popped value
        """
        if self.top > -1:
            value = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1

            return value

        print("UNDERFLOW")

    def to_string(self):
        """Return a strigified representation of the stack

        Returns:
            String: the representation of the stack
        """
        output = "Stack: "

        for i in range(self.top+1):
            if i == self.top:
                output += f"{self.stack[i]}"
                break

            output += f"{self.stack[i]}, "

        return output
