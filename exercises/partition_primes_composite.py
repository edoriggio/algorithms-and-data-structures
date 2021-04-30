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

# Complexity: O(n^2)

def partition_primes_composite(A):
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if is_prime(A[j]) and not is_prime(A[i]):
                A[i], A[j] = A[j], A[i]
                continue
            elif is_prime(A[i]):
                continue

    print(A)


def is_prime(n):
    flag = False

    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break

    return not flag


arr = [1, 10, 2, 4, 6, 9, 14, 3, 1, 6]
partition_primes_composite(arr)
