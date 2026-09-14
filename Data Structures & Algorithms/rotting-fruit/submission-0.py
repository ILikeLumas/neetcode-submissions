class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        count = 0
        maxTime = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    count += 1
                
        while q:
            row, col, time = q.popleft()

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for directionR, directionC in directions:
                newR = row + directionR
                newC = col + directionC

                if(newR in range(rows) and newC in range(cols) and grid[newR][newC] == 1):
                    grid[newR][newC] = 2
                    newTime = time + 1
                    maxTime = max(newTime, maxTime)
                    q.append((newR,newC,newTime))
                    count -= 1
        
        if count > 0:
            return -1
        else:
            return maxTime

