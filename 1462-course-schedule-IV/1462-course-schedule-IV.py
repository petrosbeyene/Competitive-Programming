class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # Floyd-Warshall Algorithm
        is_preRequsite = [[False] * numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            is_preRequsite[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    is_preRequsite[i][j] = is_preRequsite[i][j] or (is_preRequsite[i][k] and is_preRequsite[k][j])
        

        return [is_preRequsite[u][v] for u, v in queries]
                
