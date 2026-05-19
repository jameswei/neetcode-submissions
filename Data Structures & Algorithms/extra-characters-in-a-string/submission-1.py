class TrieNode:
    def __init__(self):
        self._children = {}
        self.end = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            # 遍匹配边建节点
            if char not in cur._children:
                cur._children[char] = TrieNode()
            cur = cur._children[char]
        # 单词结束，更新节点标志
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur._children:
                return False
            cur = cur._children[char]
        # 搜索的是word，有可能匹配到其他word的前缀，所以需要以标志为准
        return cur.end

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur._children:
                return False
            cur = cur._children[char]
        # 前缀匹配，无所谓是不是一个word
        return True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # 要找到最少的多余字符，那需要匹配尽可能长的word
        # 先通过给定dict构建trie树，逐个匹配，即便匹配到word也继续
        trie = TrieTree()
        for word in dictionary:
            trie.insert(word)
        
        # 分成substring，代表要连贯，从左向右
        n = len(s)

        # 三种情况：
        # char匹配，且是一个word
        # char匹配，但不是一个word
        # char不匹配

        # s="leetscode"
        # dictionary=["leet","code","leetcode"]
        min_extra_count = 2**31-1
        # [i]待匹配的字符，node已匹配的上个节点，返回最小多余字符数
        def dfs(i: int, node: TrieNode, last_pos: int, extra_count: int):
            nonlocal min_extra_count

            if i == n:
                if not node.end:
                    extra_count += n-last_pos

                min_extra_count = min(min_extra_count, extra_count)
                return

            char = s[i]

            if char in node._children:
                if node.end:
                    dfs(i, trie.root, i, extra_count)
                    dfs(i+1, node._children[char], last_pos, extra_count)
                else:
                    dfs(i+1, node._children[char], last_pos, extra_count)

            else:
                if node.end:
                    dfs(i, trie.root, i, extra_count)
                else:
                    dfs(i+1, trie.root, i+1, extra_count+i-last_pos+1)

        dfs(0, trie.root, 0, 0)
        return min_extra_count