class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graphDict = defaultdict(list)
        for s, d, cst in flights:
            graphDict[s].append([d, cst])
        
        # Dijkstra Implementation
        distances = {i: float('inf') for i in range(n)}
        distances[src] = 0

        _queue = [(0, 0, src)]
        while _queue:
            stops, dist, curr_node = heapq.heappop(_queue)
            if dist < distances[curr_node]:
                continue

            for neighbor, cst in graphDict[curr_node]:

                distance = dist + cst

                if distance < distances[neighbor] and stops <= k:

                    distances[neighbor] = distance

                    heapq.heappush(_queue, (stops + 1, distance, neighbor))
        

        return -1 if distances[dst] == float('inf') else distances[dst]
