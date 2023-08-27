class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            # reset the prefix to 0 if it doesn't help
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n 
            max_sum = max(max_sum, cur_sum)
        return max_sum
