class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for n in nums:
            word = "{:032b}".format(n)
            trie.insert(word)
        
        for n in nums:
            word = "{:032b}".format(n)
            trie.compare(word, n)
        
        return trie.maxXor


class Trie:
    def __init__(self):
        self.maxXor = 0
        self.root = {}
    
    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node:
                curr_node[c] = {}
            
            curr_node = curr_node[c]

    
    def compare(self, word, n):
        curr_node = self.root
        candidate = ""
        on, off = "1", "0"
        for c in word:
            if c == off and on in curr_node:
                candidate += on
                curr_node = curr_node[on]
            elif c == on and off in curr_node:
                candidate += off
                curr_node = curr_node[off]
            else:
                candidate += c
                curr_node = curr_node[c]
        
        val = int(candidate, 2)
        self.maxXor = max(self.maxXor, val^n)
                   


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
