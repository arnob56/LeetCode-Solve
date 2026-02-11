class Solution:
    def longestBalancedSubarray(self, nums):
        seen_even = set()
        seen_odd = set()

        balance = 0
        first_pos = {0: -1}
        ans = 0

        for i, x in enumerate(nums):
            if x % 2 == 0:
                if x not in seen_even:
                    seen_even.add(x)
                    balance += 1
            else:
                if x not in seen_odd:
                    seen_odd.add(x)
                    balance -= 1

            if balance in first_pos:
                ans = max(ans, i - first_pos[balance])
            else:
                first_pos[balance] = i

        return ans
