class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currWindow = set()
        slow  = 0
        ans = 0
        tempSize = 0
        
        for fast in range(len(s)):
            while s[fast] in currWindow:
                currWindow.remove(s[slow])
                slow += 1
                tempSize -= 1
            currWindow.add(s[fast])
            tempSize += 1
            if (tempSize > ans):
                ans = tempSize
            
        
        return ans

