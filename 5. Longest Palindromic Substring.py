class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Transform string
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n

        center = right = 0
        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Find max palindrome
        max_len = 0
        center_index = 0
        for i in range(1, n - 1):
            if p[i] > max_len:
                max_len = p[i]
                center_index = i

        start = (center_index - max_len) // 2
        return s[start:start + max_len]
