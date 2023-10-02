class TrieNode:
    def __init__(self):
        self.freq = 0
        self.children = {}

    
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}
        
    def insert(self, key: str, val: int) -> None:
        curr_val = self.map.get(key, 0)
        change = val - curr_val
        self.map[key] = val

        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.freq += change

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]

        return node.freq
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
