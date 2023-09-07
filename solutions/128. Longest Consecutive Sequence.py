class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            curr_n = n
            curr_len = 1
            while curr_n + 1 in nums_set:
                curr_len += 1
                curr_n += 1
            
            max_len = max(max_len, curr_len)

        return max_len
