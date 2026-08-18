class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        numDays = 0
        stack = []

        for i, temps in enumerate(temperatures):
            while stack and temps > stack[-1][0]:
                oldTemp, oldIndex = stack.pop()
                days = i - oldIndex
                ans[oldIndex] = days
                
            stack.append((temps, i))
        

        return ans
        

