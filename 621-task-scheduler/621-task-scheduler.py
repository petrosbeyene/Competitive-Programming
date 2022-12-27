from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        task_cntr = Counter(tasks)
        maxHeap = [-c for c in task_cntr.values()]
        heapq.heapify(maxHeap)

        deq = deque()
        time = 0
        while maxHeap or deq:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    deq.append([cnt, time+n])
            
            if deq and deq[0][1] == time:
                heapq.heappush(maxHeap, deq.popleft()[0])
        
        return time