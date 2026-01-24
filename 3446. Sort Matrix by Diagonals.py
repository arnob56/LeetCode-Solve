from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        # Step 1: collect elements by diagonal (i - j)
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        # Step 2: sort each diagonal
        for d in diagonals:
            if d >= 0:
                diagonals[d].sort(reverse=True)  # non-increasing
            else:
                diagonals[d].sort()               # non-decreasing

        # Step 3: write back sorted values
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid

