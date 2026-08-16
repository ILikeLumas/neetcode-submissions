class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        
        for i in range(k):
            temp = max(count, key=count.get)
            del count[temp]
            ans.append(temp)
        
        ans.sort()

        return ans