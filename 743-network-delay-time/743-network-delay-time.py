class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graphDict = defaultdict(list)
        for u, v, w in times:
            graphDict[u].append([v, w])

        def dijkstra(graph):
            distances = {node: float("inf") for node in range(1, n+1)}
            bfs_heap = []
            # heapq.heappush(bfs_heap, [0, k])
            bfs_heap.append([0, k])
            heapq.heapify(bfs_heap)

            # visited = set() -- no need for visited set in case of directed graph like this one
            distances[k] = 0
            while bfs_heap:
                curr_dist, curr_node = heapq.heappop(bfs_heap)
                # if curr_node in visited:
                #     continue
                
                # visited.add(curr_node)
                for neighbour in graph[curr_node]:
                    neigh, dist = neighbour
                    if curr_dist + dist < distances[neigh]:
                        distances[neigh] = curr_dist + dist
                        heapq.heappush(bfs_heap, [curr_dist+dist, neigh])
            
            return distances
        
        distances = dijkstra(graphDict)
        if float("inf") in distances.values():
            return -1
        else:
            return max(distances.values())


