class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Put the array into a set, and then check if the length 
        # of the set, is the same as the length of the original 
        # array.

        num_set = set(nums)
        if len(num_set) == len(nums):
            return False
        else:
            return True