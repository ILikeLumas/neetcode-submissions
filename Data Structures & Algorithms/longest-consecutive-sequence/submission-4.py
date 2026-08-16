class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numSet = set(nums)

        for num in nums:
            if num - 1 in numSet:
                continue

            curr = 1

            while num + curr in numSet:
                curr +=1

            longest = max(longest, curr)

        return longest
        
                


