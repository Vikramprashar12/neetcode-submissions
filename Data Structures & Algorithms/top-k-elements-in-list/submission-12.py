class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Using bucket sort, but with the index being the number of times a number 
        # shows up in the array. Updates the numbers dynamically. 

        freqArray = [ [] for i in range(len(nums) + 1) ]

        count = {}
        res = []

        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for number, frequency in count.items():
            freqArray[frequency].append(number)
        
        for i in range(len(freqArray) - 1, -1, -1):
            for c in freqArray[i]:
                res.append(c)
                if len(res) == k:
                    return res
