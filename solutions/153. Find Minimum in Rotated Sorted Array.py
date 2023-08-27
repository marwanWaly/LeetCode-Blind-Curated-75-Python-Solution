class Solution:
    def findMin(self, nums: List[int]) -> int:
        l_pointer, r_pointer = 0, len(nums) - 1
        res = nums[0]
        while l_pointer <= r_pointer:
            if nums[l_pointer] < nums[r_pointer]:
                res = min(res, nums[l_pointer])
                break
            
            mid = (l_pointer + r_pointer) // 2
            res = min(res, nums[mid])
            if nums[l_pointer] <= nums[mid]:
                l_pointer = mid + 1 
            else:
                r_pointer = mid - 1
        return res
