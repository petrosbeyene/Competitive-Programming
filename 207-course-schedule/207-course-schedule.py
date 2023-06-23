class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graphDict = defaultdict(list)
        edgeCount = [0]*numCourses
        for edge in prerequisites:
            graphDict[edge[1]].append(edge[0])
            edgeCount[edge[0]] += 1
        
        bfs_queue = deque()
        for node in range(numCourses):
            if edgeCount[node]==0:
                bfs_queue.append(node)
        
        answer = []
        while bfs_queue:
            curr = bfs_queue.popleft()
            answer.append(curr)
            for node in graphDict[curr]:
                if edgeCount[node] > 0:
                    edgeCount[node] -= 1
                if edgeCount[node] == 0:
                    bfs_queue.append(node)
        if len(answer) != numCourses:
            return False
        
        return True
