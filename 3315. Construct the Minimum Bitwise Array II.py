class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for n in nums:
            best = -1

            for k in range(31):
                if n & (1 << k):
                    x = n - (1 << k)
                    if x >= 0 and (x | (x + 1)) == n:
                        if best == -1 or x < best:
                            best = x

            ans.append(best)

        return ans

