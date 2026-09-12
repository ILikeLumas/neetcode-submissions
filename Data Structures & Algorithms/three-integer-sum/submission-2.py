class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    if [nums[i],nums[left],nums[right]] not in ans:
                        ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
        
        return ans