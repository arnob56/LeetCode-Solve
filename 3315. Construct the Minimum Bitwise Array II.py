class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for n in nums:
            # even numbers can never be formed
            if n % 2 == 0:
                ans.append(-1)
            else:
                # lowest set bit
                lsb = n & -n
                ans.append(n - lsb)

        return ans
