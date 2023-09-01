class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)
        return rob2
