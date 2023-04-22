class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def doesIntersect(i, j):
            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            return dist <= r1
        
        graphDict = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if doesIntersect(i, j):
                    graphDict[i].append(j)
        
        def dfs(node, visited):
            for child in graphDict[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)
        
        ans = 0
        for i in range(len(bombs)):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
                          
        return ans
