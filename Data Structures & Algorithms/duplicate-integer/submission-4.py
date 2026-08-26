class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use a HashMap because the search() function will take O(1)
        # In this situation, we will require Space Complexity to be O(n)
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            else:
                hashSet.add(n)
        return False