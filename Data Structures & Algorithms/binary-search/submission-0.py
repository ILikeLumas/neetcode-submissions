class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.BinarySearch(left,right,nums,target)

        
    def BinarySearch(self, left: int, right: int, nums: List[int], target: int):
        if left > right:
            return -1
        
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left = middle + 1
            return self.BinarySearch(left, right, nums, target)
        else:
            right = middle - 1
            return self.BinarySearch(left, right, nums, target)
    