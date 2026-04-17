class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixTreeNode()
            cur = cur.children[c]
        
        cur.is_word = True

    def is_a_word(self, content: str) -> bool:
        cur = self.root

        for c in content:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.is_word

    def is_a_prefix(self, content: str) -> bool:
        cur = self.root

        for c in content:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a prefix tree
        # and insert all given words
        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        res = set()

        def dfs(i: int, j: int, node: PrefixTreeNode, chars: list[str]):
            if i > m-1 or i < 0 or j > n-1 or j < 0:
                return

            if visited[i][j]:
                return

            if len(node.children) == 0:
                return
            
            cur_char = board[i][j]
            if cur_char not in node.children:
                return

            chars.append(cur_char)
            visited[i][j] = True

            cur_node = node.children[cur_char]
            if cur_node.is_word:
                res.add(''.join(chars))

            dfs(i, j+1, cur_node, chars)
            dfs(i, j-1, cur_node, chars)
            dfs(i+1, j, cur_node, chars)
            dfs(i-1, j, cur_node, chars)

            chars.pop()
            visited[i][j] = False
            return


        # traverse board and search in prefix tree
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, list())
        
        return list(res)