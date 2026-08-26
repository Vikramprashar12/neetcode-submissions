class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*len(nums)

        prefix = 1
        for c in range(len(nums)):
            res[c] = prefix
            prefix *= nums[c]

        postfix = 1
        for c in range(len(nums)-1, -1, -1):
            res[c]*=postfix
            postfix*=nums[c]

        return res

        