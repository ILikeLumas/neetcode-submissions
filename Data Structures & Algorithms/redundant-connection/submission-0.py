class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        
        def dfs(node, parent):
            if visited[node]:
                return True

            visited[node] = True
            for nextNode in adj[node]:
                if nextNode == parent:
                    continue
                if dfs(nextNode, node):
                    return True
            return False

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            visited = [False] * (n + 1)

            if dfs(i, -1):
                return [i,j]

        return []            
