
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums): ## iterate nums and tracks index i
            c = target - num
            if c in num_to_index:
                return [num_to_index[c], i]
            num_to_index[num] = i

        
'''
In Summary:

This solution efficiently finds the indices of the two numbers that sum up to the target by:

    Using a dictionary to store the indices of encountered numbers.
    Calculating the complement of each number.
    Checking if the complement has already been encountered.
    Returning the indices of the two numbers if the complement is found.

This approach has a time complexity of O(n) because it iterates through the nums list only once.
'''