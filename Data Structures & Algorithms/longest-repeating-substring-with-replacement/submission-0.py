class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        count = {}
        slow = 0
        maxFreq = 0

        for fast in range(len(s)):
            count[s[fast]] = count.get(s[fast],0) + 1
            maxFreq = max(maxFreq, count[s[fast]])
            
            while (fast - slow + 1) - maxFreq > k:
                count[s[slow]] -= 1
                slow += 1
            
            ans = max(ans, fast - slow + 1)

        return ans
            
                

        