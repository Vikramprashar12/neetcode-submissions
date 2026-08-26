class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Using bucket sort, but with the index being the number of times a number 
        # shows up in the array. Updates the numbers dynamically. 

        holder = [[] for i in range(len(nums) + 1)]
        count = {}
        res = list()

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, frequency in count.items():
            holder[frequency].append(num)
        
        for index in range(len(holder)-1,0, -1):
            
            for n in holder[index]:
                res.append(n)
                if len(res)==k:
                    return res
