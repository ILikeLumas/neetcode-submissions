class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = {}
        rows = len(grid)
        cols = len(grid[0])             
        q = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,0))

        while q:
            row, col, dist = q.popleft()

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for directionR, directionC in directions:
                newRow = row + directionR
                newCol = col + directionC
                if(newRow in range(rows) and newCol in range(cols) and (newRow,newCol) not in visited and grid[newRow][newCol] == 2147483647):
                    newDist = dist + 1
                    visited[(newRow, newCol)] = newDist
                    grid[newRow][newCol] = newDist
                    q.append((newRow,newCol,newDist))
        
         
            


