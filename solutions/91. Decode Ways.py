class Solution:
    def numDecodings(self, s: str) -> int:
        x, y, z = 1, 0, 0
        # in first loop [..., x]y, z
        # in second loop [..., x, y] z
        # in third loop [..., x, y, z]
        for i in range(len(s) - 1, -1, -1):
            x, y, z = 0, x, y
            if s[i] == '0':
                x = 0
                continue
            else:
                x = y

            if i + 1 != len(s) and 1 <= int(s[i:i+2]) <= 26:
                x += z
        return x
