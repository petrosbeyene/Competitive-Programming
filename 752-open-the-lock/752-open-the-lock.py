class Solution:
    def children(self, lock):
        children = []
        for i in range(4):
            turned = str((int(lock[i])+1)%10)
            child = lock[:i]+turned+lock[i+1:]
            children.append(child)

            turned = str((int(lock[i]) - 1 + 10)%10)
            child = lock[:i]+turned+lock[i+1:]
            children.append(child)
        
        return children

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        bfs_q = deque()
        bfs_q.append(["0000", 0])
        visited = set(deadends)
        visited.add("0000")
        while bfs_q:
            lock, turn= bfs_q.popleft()
            if lock == target:
                return turn
            
            for child in self.children(lock):
                if child not in visited:
                    visited.add(child)
                    bfs_q.append([child, turn+1])
        
        return -1
