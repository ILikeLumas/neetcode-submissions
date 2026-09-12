class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = 0
        while rows + 1 < len(matrix) and target >= matrix[rows + 1][0]:
            rows += 1
        numCol = len(matrix[rows])
        low = 0
        high = numCol - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[rows][mid] > target:
                high = mid - 1
            elif matrix[rows][mid] < target:
                low = mid + 1
            else:
                return True
        
        return False