class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # If only spaces or empty
        if i == n:
            return 0

        # 2. Handle sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Overflow check BEFORE adding digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
