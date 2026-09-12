class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        minK = 1
        ans = maxK
        if(len(piles) == h):
            return ans
        while minK <= maxK:
            testK = ((maxK + minK) // 2)
            totalHours = sum((pile + testK - 1) // testK for pile in piles)
            if totalHours > h:
                minK = testK + 1
            else:
                ans = testK
                maxK = testK - 1
        return ans

        