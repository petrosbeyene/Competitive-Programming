class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str, currIdx: int) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            
            curr_node = curr_node.children[c]
            curr_node.wordIdx = currIdx
    
    
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            if c not in curr_node.children:
                return -1
            
            curr_node = curr_node.children[c]
        
        return curr_node.wordIdx
        
                
        
class TrieNode:
    def __init__(self):
        self.wordIdx = None
        self.children = {}
        


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for i, word in enumerate(words):

            for j in range(len(word)-1, -1, -1):
                curr_word = word[j:] + '#' + word
                self.trie.insert(curr_word, i)
        
    def f(self, pref: str, suff: str) -> int:
        word = suff + '#' + pref
        ans = self.trie.startsWith(word)

        return ans


        



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
