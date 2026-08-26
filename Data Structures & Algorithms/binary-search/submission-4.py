class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = ((r-l)//2)+l
            if nums[l] == target: return l
            if nums[r] == target: return r
            print(l, r, mid)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1