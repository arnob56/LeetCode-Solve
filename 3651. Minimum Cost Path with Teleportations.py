import heapq

class Solution:
    def minimumCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        # dist[i][j][t]
        dist = [[[INF]*(k+1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0
        
        # all cells sorted by value
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))
        
        # pointer for each teleport count
        ptr = [0]*(k+1)
        used = [[False]*len(cells) for _ in range(k+1)]
        
        pq = [(0, 0, 0, 0)]  # cost, i, j, t
        
        while pq:
            cost, i, j, t = heapq.heappop(pq)
            if cost != dist[i][j][t]:
                continue
            
            # normal moves
            for ni, nj in ((i+1,j),(i,j+1)):
                if ni < m and nj < n:
                    nc = cost + grid[ni][nj]
                    if nc < dist[ni][nj][t]:
                        dist[ni][nj][t] = nc
                        heapq.heappush(pq, (nc, ni, nj, t))
            
            # teleport moves
            if t < k:
                while ptr[t] < len(cells) and cells[ptr[t]][0] <= grid[i][j]:
                    _, x, y = cells[ptr[t]]
                    if not used[t][ptr[t]]:
                        used[t][ptr[t]] = True
                        if cost < dist[x][y][t+1]:
                            dist[x][y][t+1] = cost
                            heapq.heappush(pq, (cost, x, y, t+1))
                    ptr[t] += 1
        
        return min(dist[m-1][n-1])
