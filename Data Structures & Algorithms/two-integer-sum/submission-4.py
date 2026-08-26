class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        a = 0
        for num in nums:
            if (target-num) not in res:
                print(target-num)
                res[num] = nums.index(num)
                print(res)
            else:
                return [ res[target-num], a]

            a += 1