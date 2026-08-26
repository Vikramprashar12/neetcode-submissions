class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index, num in enumerate(nums):
            if target-num in res:
                return [res[target-num], index]
            res[num] = index