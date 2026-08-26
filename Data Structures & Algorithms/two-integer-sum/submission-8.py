class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = {} # Key should be num, and value should be the index

        for index, num in enumerate(nums):
            if target-num in helper:
                return [helper[target-num], index]
            helper[num] = index
            