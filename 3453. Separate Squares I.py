class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        eps = 1e-6
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        def diff(y_line: float) -> float:
            below = 0
            total = 0
            for _, y, l in squares:
                total += l * l
                if y + l <= y_line:
                    below += l * l
                elif y < y_line < y + l:
                    below += l * (y_line - y)
            return below - total / 2  # positive means too low

        while high - low > eps:
            mid = (low + high) / 2
            if diff(mid) < 0:
                low = mid
            else:
                high = mid

        return low
