class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longest_consecutive(bars):
            bars.sort()
            longest = 1
            current = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current += 1
                else:
                    current = 1
                longest = max(longest, current)
            return longest
        
        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)
        side = min(max_h + 1, max_v + 1)
        return side * side
