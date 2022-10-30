class Solution:
    def maxArea(self, height) -> int:
        left = 0
        maxWidth = right = len(height) - 1

        maxArea = 0
        for w in range(maxWidth, 0, -1):
            if height[left] < height[right]:
                maxArea = max(maxArea, w*height[left])
                left += 1
            else:
                maxArea = max(maxArea, w*height[right])
                right -= 1
        
        return maxArea