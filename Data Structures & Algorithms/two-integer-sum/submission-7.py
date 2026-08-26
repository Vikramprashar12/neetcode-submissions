class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, num in enumerate(nums):
            if target-num in hashMap:
                return [hashMap[target-num],index]
            if num not in hashMap:
                hashMap[num] = index