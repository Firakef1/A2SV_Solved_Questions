class Solution:
    def maxArea(self, height: List[int]) -> int:

        left , right = 0, len(height)-1

        left_element =  height[left]
        right_element = height[right]

        max_area = 0
        while left < right:
            new_area = min([left_element, right_element])*(right-left)
            if max_area < new_area:

                max_area = new_area
            
            if left_element < right_element:

                left += 1

                left_element =  height[left]
            
            else:

                right -= 1
                right_element = height[right]
        
        return max_area
        




        