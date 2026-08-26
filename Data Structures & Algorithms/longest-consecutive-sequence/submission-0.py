class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)

        if len(nums)==0:
            return 0

        for num in s:
            if num-1 not in s:
                length=0
                while num+length in s:
                    length+=1
                res = max(res, length)
        return res

            
        