'''
Given a list of integers nums and a target, return the indices of the two numbers that add up to target. Exactly one solution exists, and you can't use the same element twice.
'''

def two_sum(nums:list[int], target:int ) -> list:
    seen = {}
    
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


assert two_sum([2,7,11,15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]

