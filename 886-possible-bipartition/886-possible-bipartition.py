class Solution:
    def dfs(self, node, graphDict, clrDict, currClr):
        clrDict[node] = currClr
        for neigh in graphDict[node]:
            if clrDict[neigh] == currClr:
                return False
            elif clrDict[neigh] == -1:
                if not self.dfs(neigh, graphDict, clrDict, 1-currClr):
                    return False
        
        return True
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graphDict = defaultdict(list)
        for ls in dislikes:
            graphDict[ls[0]].append(ls[1])
            graphDict[ls[1]].append(ls[0])
        
        clrDict = {}
        for i in range(1, n+1):
            clrDict[i] = -1
        
        for i in range(1, n+1):
            if clrDict[i] == -1:
                if not self.dfs(i, graphDict, clrDict, 0):
                    return False
        
        return True
