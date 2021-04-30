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

# Complexity: O(n)

def like_or_dislike(A):
    like_dislike = 0

    for i in A:
        if i == "like":
            like_dislike += 1
        else:
            like_dislike -= 1

    if like_dislike == 0:
        return "Undecided"
    elif like_dislike > 0:
        return "Like"
    else:
        return "Dislike"


arr = ["like", "dislike", "like", "like"]
print(like_or_dislike(arr))
