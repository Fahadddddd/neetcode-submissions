class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        max_area = 0

        while high > low:
            curr_arr = min(heights[high], heights[low] ) * (high - low)
            max_area = max(max_area,curr_arr)
        
            if heights[low] > heights[high]:
                high -= 1
            else:
                low += 1
            
        return max_area

         
            
