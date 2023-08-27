class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_pointer, r_pointer = 0, len(nums) - 1
        while l_pointer <= r_pointer:
            mid = (l_pointer + r_pointer) // 2
            if nums[mid] == target:
                return mid
        
            if nums[l_pointer] <= nums[mid]:
                if target > nums[mid] or target < nums[l_pointer]:
                    l_pointer = mid + 1
                else:
                    r_pointer = mid - 1
            else:
                if target < nums[mid] or target > nums[r_pointer]:
                    r_pointer = mid - 1
                else:
                    l_pointer = mid + 1
        return -1
