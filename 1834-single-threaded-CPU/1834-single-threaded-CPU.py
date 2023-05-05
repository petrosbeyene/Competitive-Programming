class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, val in enumerate(tasks):
            tasks[i].append(i)
        
        tasks.sort(key=lambda t: t[0])
        res, minHeap = [], []
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if minHeap:
                process_time, idx = heapq.heappop(minHeap)
                res.append(idx)
                time += process_time
            else:
                time = tasks[i][0]
        
        return res

