class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            
            curr_node = curr_node.children[c]
        
        curr_node.is_end = True

    def search(self, word: str, def_root = None) -> bool:
        if def_root == None:
            curr_node = self.root
        else:
            curr_node = def_root

        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for key in curr_node.children.keys():
                    if self.search(word[i+1:], curr_node.children[key]):
                        return True
                
                return False
            elif c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return False

        return curr_node.is_end

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
