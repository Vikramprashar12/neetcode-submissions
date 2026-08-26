class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Integer array, negative and positive values.
        # Array will be atleast of size 1 (Don't need to take care of edge case: null)    

        # HashMap -> O(n)
        # Brute Force Approach -> O(n^2)

        hashSet = set()
        for n in nums: 
            if n in hashSet:
                return True
            else:
                hashSet.add(n)
        return False