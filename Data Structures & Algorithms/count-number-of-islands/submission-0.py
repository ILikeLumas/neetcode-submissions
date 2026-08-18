class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for directionRow, directionCol in directions:
                    r, c = row + directionRow, col + directionCol

                    if(r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i, j)
                    islands += 1
        
        return islands
