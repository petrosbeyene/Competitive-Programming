class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graphDict = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graphDict[u].append([v, values[i]])
            graphDict[v].append([u, (1/values[i])])
        
        def dfs(curr_node, graph, target, ans, visited):
            if target not in graph or curr_node not in graph:
                return -1

            if curr_node == target:
                return ans
            
            visited.add(curr_node)
            original_ans = ans
            for neigh, val in graph[curr_node]:
                if neigh not in visited:
                    result = dfs(neigh, graph, target, ans * val, visited)
                    if result != -1:
                        return result
            
            return -1
        
        ans = []
        for start, dest in queries:
            visited = set()
            ans.append(dfs(start, graphDict, dest, 1, visited))
        
        return ans
