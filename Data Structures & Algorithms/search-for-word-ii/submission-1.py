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

        def dfs(i: int, j: int, chars: list[str]):
            # 越界
            if i > m-1 or i < 0 or j > n-1 or j < 0:
                return

            # 访问过
            if visited[i][j]:
                return
            
            cur_char = board[i][j]
            visited[i][j] = True

            # 做选择
            chars.append(cur_char)
            word = ''.join(chars)

            if trie.is_a_word(word):
                # 已经匹配到word的情况下还要沿着这条路径继续dfs吗？
                # 能，因为后续可能还会匹配到新的word，可以作为一个新结果
                res.add(word)
                dfs(i, j+1, chars)
                dfs(i, j-1, chars)
                dfs(i-1, j, chars)
                dfs(i+1, j, chars)
            elif trie.is_a_prefix(word):
                # 如果不是一个word，但是一个word的prefix
                # 所以可以继续延续这条路径
                dfs(i, j+1, chars)
                dfs(i, j-1, chars)
                dfs(i-1, j, chars)
                dfs(i+1, j, chars)

            # else:
            # 连prefix都不是，放弃这条路径

            # 撤销选择
            chars.pop()
            visited[i][j] = False
            return


        # traverse board and search in prefix tree
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    dfs(i, j, list())
        return list(res)