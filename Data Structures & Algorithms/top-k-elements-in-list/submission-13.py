class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Insert into HashMap, Key: Num, Value: Frequency

        count = {}
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        print(count)

        BucketSort = [[] for i in range(len(nums)+1)]
        print(BucketSort)

        for num, freq in count.items():
            print(num, freq)
            BucketSort[freq].append(num)

        print(BucketSort)
        counter = k
        for i in range(len(BucketSort)-1, 0, -1):
            print("I", i)
            for c in BucketSort[i]:
                res.append(c)
                if len(res)==k:
                    return res
        
        