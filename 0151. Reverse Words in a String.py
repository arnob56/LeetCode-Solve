class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()          # removes extra spaces
        words.reverse()            # reverse word order
        return " ".join(words)     # single space join
