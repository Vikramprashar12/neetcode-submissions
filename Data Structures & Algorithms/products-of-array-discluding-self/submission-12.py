class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        runningSum = 1
        for n in nums:
            res.append(runningSum)
            runningSum  = runningSum * n
        
        runningSum = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * runningSum
            runningSum  = runningSum * nums[i]
        return res
