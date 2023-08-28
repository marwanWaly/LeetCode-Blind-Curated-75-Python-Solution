class Solution:
    def hammingWeight(self, n: int) -> int:
        number_of_ones = 0
        for i in range(32):
            if n & 1:
                number_of_ones += 1
            n >>= 1
        return number_of_ones
