

import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        
        # nums[0] is always included
        base = nums[0]
        
        # We need to choose (k-1) elements from nums[1:]
        need = k - 1
        
        # Max heap for chosen elements (store negative values)
        small = []
        # Min heap for remaining elements
        large = []
        
        sum_small = 0
        removed = defaultdict(int)
        
        def clean(heap):
            while heap and removed[heap[0]]:
                removed[heap[0]] -= 1
                heapq.heappop(heap)
        
        def rebalance():
            nonlocal sum_small
            clean(small)
            clean(large)
            
            while len(small) > need:
                val = -heapq.heappop(small)
                sum_small -= val
                heapq.heappush(large, val)
            
            while len(small) < need and large:
                val = heapq.heappop(large)
                sum_small += val
                heapq.heappush(small, -val)
        
        ans = float("inf")
        L = 1
        
        for R in range(1, n):
            # Add nums[R]
            if len(small) < need:
                heapq.heappush(small, -nums[R])
                sum_small += nums[R]
            else:
                if small and nums[R] < -small[0]:
                    val = -heapq.heappop(small)
                    sum_small -= val
                    heapq.heappush(large, val)
                    heapq.heappush(small, -nums[R])
                    sum_small += nums[R]
                else:
                    heapq.heappush(large, nums[R])
            
            # Shrink window if too large
            while R - L + 1 > dist + 1:
                if small and nums[L] <= -small[0]:
                    removed[-nums[L]] += 1
                    sum_small -= nums[L]
                else:
                    removed[nums[L]] += 1
                L += 1
                rebalance()
            
            # Update answer
            if len(small) == need:
                ans = min(ans, base + sum_small)
        
        return ans
