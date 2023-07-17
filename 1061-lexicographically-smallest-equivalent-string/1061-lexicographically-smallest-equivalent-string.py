class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = UnionFind()
        
        for i in range(len(s1)):
            graph.union((ord(s1[i])-ord('a')), (ord(s2[i])-ord('a')))
        
        ans = ""
        for c in baseStr:
            ans += chr(graph.find(ord(c) - ord('a')) + ord('a'))
        
        return ans



class UnionFind:
    def __init__(self):
        self.root = [i for i in range(26)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if rootX < rootY:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
        else:
            return
