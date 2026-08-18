class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(row, col):
            q = collections.deque()
            q.append((row,col))
            visited.add((row,col))
            size = 1
            
            while q:
                row, col = q.popleft()

                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for directionRow, directionCol in directions:
                    newRow = directionRow + row
                    newCol = directionCol + col
                    if (newRow in range(rows) and 
                    newCol in range(cols) and 
                    grid[newRow][newCol] == 1 and 
                    (newRow, newCol) not in visited):
                        q.append((newRow, newCol))
                        visited.add((newRow,newCol))
                        size += 1
            
            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    tempSize = bfs(i,j)
                    if tempSize > maxArea:
                        maxArea = tempSize
        
        return maxArea
                

