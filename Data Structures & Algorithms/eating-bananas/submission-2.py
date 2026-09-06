class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = 0

        while l <= r:
            m = (l+r)//2
            print(m)
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours <= h:
                res = m
                r = m-1
            elif hours > h:
                l = m+1
        return res