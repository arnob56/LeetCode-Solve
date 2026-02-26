class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left (ignore MSB)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                # Odd case
                steps += 2
                carry = 1
            else:
                # Even case
                steps += 1
        
        return steps + carry
