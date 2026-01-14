from bisect import bisect_left

class Solution:
    def separateSquares(self, squares):
        # Step 1: Collect events for vertical sweep
        events = []  # (y, x1, x2, type)
        for x, y, l in squares:
            events.append((y, x, x + l, 1))      # Add square at bottom edge
            events.append((y + l, x, x + l, -1)) # Remove at top edge
        
        events.sort()  # Sort by y (sweep from bottom to top)
        
        # Step 2: Sweep through y-levels and compute cumulative area
        active = []  # list of active x-intervals
        prev_y = events[0][0]
        area = 0
        area_curve = [(prev_y, 0)]  # (y, total_area_below_y)
        
        for y, x1, x2, typ in events:
            # compute covered width using active x-intervals
            width = self._compute_union_width(active)
            area += width * (y - prev_y)
            area_curve.append((y, area))
            
            # update active intervals
            if typ == 1:
                active.append((x1, x2))
            else:
                # safely remove (since exact tuple may exist multiple times)
                active.remove((x1, x2))
            
            prev_y = y
        
        total_area = area_curve[-1][1]
        half_area = total_area / 2
        
        # Step 3: Binary search for y where area crosses half_area
        ys = [y for y, _ in area_curve]
        areas = [a for _, a in area_curve]
        
        idx = bisect_left(areas, half_area)
        if idx == 0:
            return float(ys[0])
        if idx == len(areas):
            return float(ys[-1])
        
        # Step 4: Linear interpolation for precision
        y1, a1 = ys[idx - 1], areas[idx - 1]
        y2, a2 = ys[idx], areas[idx]
        if abs(a2 - a1) < 1e-12:
            return float(y1)
        return float(y1 + (half_area - a1) * (y2 - y1) / (a2 - a1))
    
    
    def _compute_union_width(self, intervals):
        """Merge x-intervals and compute total covered width."""
        if not intervals:
            return 0
        
        intervals = sorted(intervals)
        merged = []
        for s, e in intervals:
            if not merged or merged[-1][1] < s:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
        return sum(e - s for s, e in merged)
