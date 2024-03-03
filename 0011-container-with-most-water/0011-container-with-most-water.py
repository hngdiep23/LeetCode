class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            m = min(height[left], height[right])
            cal = (right - left) * m
            if cal > area:
                area = cal
            a1 = min(height[left + 1], height[right])
            a2 = min(height[left], height[right - 1])
            if a1 > m:
                left += 1
            elif a2 > m:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1
        return area