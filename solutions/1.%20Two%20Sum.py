class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {} # val: index
        for i, n in enumerate(nums):
            diff = target-n
            if diff in holder:
                return [holder[diff], i]
            else:
                holder[n] = i
