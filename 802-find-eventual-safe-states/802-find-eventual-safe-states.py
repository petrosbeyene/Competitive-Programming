class Solution:
    def dfs(self, graph, node, safe):
        if node in safe:
            return safe[node]
        
        safe[node] = False
        for neigh in graph[node]:
            if not self.dfs(graph, neigh, safe):
                return safe[node]
        
        safe[node] = True
        return safe[node]

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        ans = []
        for i in range(len(graph)):
            if self.dfs(graph, i, safe):
                ans.append(i)
        
        return ans
