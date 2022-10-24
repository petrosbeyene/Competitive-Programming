import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        while len(stones) > 0:
            if len(stones) == 1:
                return -stones[0]
            
            first_elem = heapq.heappop(stones)
            second_elem = heapq.heappop(stones)
            if first_elem != second_elem:
                heapq.heappush(stones, first_elem - second_elem)
        
        return 0