class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graphDict = defaultdict(list)
        for idx, (u, v) in enumerate(edges):
            graphDict[u].append([v, succProb[idx]])
            graphDict[v].append([u, succProb[idx]])
        
        def dijkstra(graph):
            probabilities = {node: float("inf") for node in range(n)}
            heap = []
            
            heap.append([-1, start_node])
            heapq.heapify(heap)

            visited = set()
            probabilities[start_node] = 1
            while heap:
                curr_prob, curr_node = heapq.heappop(heap)
                if curr_node in visited:
                    continue
                
                visited.add(curr_node)
                for neigh, prob in graph[curr_node]:
                    if (curr_prob * prob) < probabilities[neigh]:
                        
                        probabilities[neigh] = curr_prob * prob
                        # We are basically using maxheap, with negative values
                        heapq.heappush(heap, [curr_prob * prob, neigh])
            
            return probabilities

        probabilities = dijkstra(graphDict)

        return -probabilities[end_node] if probabilities[end_node] != float("inf") else 0
