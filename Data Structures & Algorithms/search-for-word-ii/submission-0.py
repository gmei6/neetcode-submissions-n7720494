class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # Stores the word ending at this node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word # Mark the end of a valid word
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        # 2. Define the DFS
        def dfs(r, c, node):
            # Base cases: out of bounds, already visited, or char not in Trie
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            
            # If we found a word, add it to our result set
            if node.word:
                res.add(node.word)
                
            # Explore all 4 adjacent directions
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            
            # Backtrack: remove from visited so it can be used in other paths
            visit.remove((r, c))
            
        # 3. Traverse the board once
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return list(res)