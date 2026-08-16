class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        index1 = {}
        index2 = {}
        for i in range(len(s)):
            if s[i] not in index1:
                index1[s[i]] = 1
            else:
                index1[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in index2:
                index2[t[i]] = 1
            else:
                index2[t[i]] += 1
        
        if index1 == index2:
            return True
        else:
            return False
