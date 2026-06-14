class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        # First check if the letter already exists
        # If the letter doesn't already exist, then
        # we will add the letter to the dictionary
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.word = True
        
    def search(self, word: str) -> bool:
        return self.recursive_search(word, 0, self.root)

    def recursive_search(self, word: str, index: int, curr: Node) -> bool:
        while index < len(word):
            char = word[index]
            if char == ".":
                # Consider the case where the word is valid until the last char, and 
                # the last char is a .

                for child in curr.children.values():
                    if self.recursive_search(word, index + 1, child):
                        return True
                return False
            else:
                if char not in curr.children:
                    return False
                curr = curr.children[char]
                index += 1
        return curr.word







