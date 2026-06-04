# This creates a new class
class TrieNode:
    def __init__(self):
        self.children = {}          # This creates the hashmap
        self.endOfWord = False 

class PrefixTree:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root 
        for char in word:
            if char not in curr_node.children:
                temp = TrieNode()
                curr_node.children[char] = temp
                curr_node = temp
            else:
                curr_node = curr_node.children[char]
        curr_node.endOfWord = True


    def search(self, word: str) -> bool:
        curr_node = self.root 
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root 
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True