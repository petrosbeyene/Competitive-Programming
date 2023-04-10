class Solution:
    def dfs(self, node, visited, graph):
        if node in visited:
            return
        
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                self.dfs(neighbour, visited, graph)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph_dict = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph_dict[i].append(j)
        

        visited = set()
        n = len(isConnected)
        cnt = 0
        for i in range(n):
            if i not in visited:
                self.dfs(i, visited, graph_dict)
                cnt += 1
        
        return cnt
