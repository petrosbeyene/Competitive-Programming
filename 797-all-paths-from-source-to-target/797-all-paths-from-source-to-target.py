class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        tempSolution = []
        def dfs(node):
            if node == len(graph)-1:
                ans.append(tempSolution[:])
                return
            
            for i in graph[node]:
                tempSolution.append(i)
                dfs(i)
                tempSolution.pop()
        
        tempSolution.append(0)
        dfs(0)

        return ans
