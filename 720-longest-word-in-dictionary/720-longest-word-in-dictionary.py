class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        ans = ""
        for idx, w in enumerate(words):
            if (trie.startsWith(w[:-1]) or len(w) == 1) and len(w) > len(ans):
                ans = w

            if not trie.startsWith(w[:-1]) and len(w) > 1:
                continue
            else:
                val = trie.insert(w)
    
        return ans

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:        
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            
            curr_node = curr_node.children[c]
        
        curr_node.is_end = True

    
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            if c not in curr_node.children:
                return False
            
            curr_node = curr_node.children[c]
        
        return True
                
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        
