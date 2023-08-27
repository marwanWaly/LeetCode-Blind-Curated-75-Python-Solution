class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_max, cur_max, cur_min = nums[0], 1, 1
        for n in nums:
            temp = cur_max
            cur_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, n * temp, n * cur_min)
            prod_max = max(prod_max, cur_max)
        return prod_max
