class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = []
        for word in words:

            prefix_score = trie.calculateScore(word)
            ans.append(prefix_score)
        
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
            curr_node.count += 1

    
    def calculateScore(self, word: str) -> int:
        curr_node = self.root
        score = 0
        for c in word:
            curr_node = curr_node.children[c]
            score += curr_node.count

        return score
        
                
        
class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        
