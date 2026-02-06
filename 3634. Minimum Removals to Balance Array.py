class Solution:
    def minimumRemovals(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l = 0
        max_len = 1
        n = len(nums)
        
        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return n - max_len
