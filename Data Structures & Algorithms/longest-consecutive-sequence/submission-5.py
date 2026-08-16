class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dic = defaultdict(int)
        ans = 0

        for number in nums:
            if not dic[number]:
                dic[number] = dic[number - 1] + dic[number + 1] + 1
                dic[number - dic[number - 1]] = dic[number]
                dic[number + dic[number + 1]] = dic[number]
                ans = max(ans, dic[number])
        return ans
        
                


