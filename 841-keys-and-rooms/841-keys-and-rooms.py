class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        bfs_queue = deque()
        bfs_queue.append(0)

        visited = set()
        visited.add(0)
        while bfs_queue:
            val = bfs_queue.popleft()
            for child in rooms[val]:
                if child not in visited:
                    visited.add(child)
                    bfs_queue.append(child)
        
        return len(visited)==len(rooms)
