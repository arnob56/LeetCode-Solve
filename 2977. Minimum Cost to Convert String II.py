from collections import defaultdict
import math

class Solution:
    def minimumCost(self, source: str, target: str, original, changed, cost) -> int:
        n = len(source)

        # ---- Step 1: Group rules by substring length ----
        rules_by_len = defaultdict(list)
        lengths = set()

        for o, c, w in zip(original, changed, cost):
            L = len(o)
            rules_by_len[L].append((o, c, w))
            lengths.add(L)

        # ---- Step 2: Precompute minimum cost for each length using Floyd Warshall ----
        # dist[L][s][t] = minimum cost to convert s -> t (len L)
        dist = {}

        for L, rules in rules_by_len.items():
            # collect unique strings of this length
            strings = set()
            for o, c, _ in rules:
                strings.add(o)
                strings.add(c)

            strings = list(strings)
            idx = {s: i for i, s in enumerate(strings)}
            m = len(strings)

            # distance matrix
            d = [[math.inf] * m for _ in range(m)]
            for i in range(m):
                d[i][i] = 0

            for o, c, w in rules:
                d[idx[o]][idx[c]] = min(d[idx[o]][idx[c]], w)

            # Floyd Warshall
            for k in range(m):
                for i in range(m):
                    if d[i][k] == math.inf:
                        continue
                    for j in range(m):
                        if d[k][j] == math.inf:
                            continue
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j])

            dist[L] = (idx, strings, d)

        # ---- Step 3: DP over positions ----
        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == math.inf:
                continue

            # Case 1: single char already matches
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            # Case 2: try substring transformations
            for L in lengths:
                j = i + L
                if j > n:
                    continue

                s_sub = source[i:j]
                t_sub = target[i:j]

                if s_sub == t_sub:
                    dp[j] = min(dp[j], dp[i])
                    continue

                if L not in dist:
                    continue

                idx_map, strings, d = dist[L]

                if s_sub in idx_map and t_sub in idx_map:
                    u = idx_map[s_sub]
                    v = idx_map[t_sub]
                    if d[u][v] != math.inf:
                        dp[j] = min(dp[j], dp[i] + d[u][v])

        return -1 if dp[n] == math.inf else dp[n]
