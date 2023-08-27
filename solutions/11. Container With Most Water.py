class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l_pointer, r_pointer = 0, len(height) - 1
        while l_pointer <= r_pointer:
            
            if height[l_pointer] < height[r_pointer]:
                max_area = max(max_area,  height[l_pointer] * (r_pointer - l_pointer))
                l_pointer += 1
            else:
                max_area = max(max_area,  height[r_pointer] * (r_pointer - l_pointer))
                r_pointer -= 1
                
        return max_area
