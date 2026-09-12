class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        totalArea = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                index = stack.pop()
                if stack:
                    totalArea = totalArea + (min(height[stack[-1]],height[i]) - height[index]) * (i - stack[-1] - 1)
            stack.append(i)
        return totalArea
            
        

