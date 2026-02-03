class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # 1. strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False  # no increasing part

        p = i

        # 2. strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == p:
            return False  # no decreasing part

        q = i

        # 3. strictly increasing again
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
