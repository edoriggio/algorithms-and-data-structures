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

# Problem:
# Write an algorithm Partition-Primes-Composites(A) that takes an array A
# of n integers such that 1 < A[i] ≤ m for all i, and partitions A in-place
# so that all primes precede all composites in A. Analyze the complexity of
# your solution as a function of n and m. Recall that an integer greater
# than 1 is prime if it is divisible by only two positive integers (itself
# and 1) or otherwise it is composite.

# Complexity:
# O(n)

def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return False

def partition_primes_composite(array):
    i = 0

    for j in range(1, len(array)):
        if(is_prime(array[j])):
            array[i], array[j] = array[j], array[i]
            i += 1

    return array

print(partition_primes_composite([1,5,12,7,3,11,14,13,17]))
