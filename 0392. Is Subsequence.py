class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s

        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1

        return i == len(s)
