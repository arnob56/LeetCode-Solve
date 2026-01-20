from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            # Even numbers cannot be formed
            if n % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s
            k = 0
            temp = n
            while temp & 1:
                k += 1
                temp >>= 1

            # Subtract 2^(k-1)
            ans.append(n - (1 << (k - 1)))

        return ans
