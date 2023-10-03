class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        trie.insert(s)

        ans = 0
        cache = defaultdict(bool)
        for word in words:
            if word in cache:
                ans += cache[word]
            else:
                val = trie.bfs_search(word)
                ans += val
                cache[word] = val 
        
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
    
    def bfs_search(self, word: str) -> bool:
        bfs_q = deque()
        bfs_q.append(self.root)
        i = 0
        while bfs_q:
            curr_node = bfs_q.popleft()
            
            if i == len(word):
                return True

            if word[i] in curr_node.children:
                bfs_q.append(curr_node.children[word[i]])
                i += 1
            else:
                for child in curr_node.children:
                    bfs_q.append(curr_node.children[child])
        
        return False        
                
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        
