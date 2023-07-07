class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = UnionFind(len(edges)+1)
        
        for n1, n2 in edges:
            if not graph.union(n1, n2):
                return [n1, n2]


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        else:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
        
        return True
