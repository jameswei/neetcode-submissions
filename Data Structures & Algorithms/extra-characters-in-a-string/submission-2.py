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
        # s="leetscode", dictionary=["leet","code","leetcode"]
        # s = "neetcodde", dictionary = ["neet","code","neetcode"]

        # 要找到最少的多余字符，那需要尽可能多的匹配，同时substring要求连续
        # 先通过给定dict构建trie树
        trie = TrieTree()
        for word in dictionary:
            trie.insert(word)
        
        # 分成substring，代表要连贯，从左向右
        n = len(s)

        # [i]待匹配的字符，[i:]最少的多余字符
        def dfs(i: int) -> int:
            if i == n:
                return 0

            min_extra = n-i
            # 把s[i]当作多余字符，从i+1尝试匹配
            min_extra = min(min_extra, 1+dfs(i+1))

            # 从i尝试匹配
            cur_node = trie.root
            cur_pos = i
            
            while cur_pos < n and s[cur_pos] in cur_node._children:
                cur_node = cur_node._children[s[cur_pos]]
                cur_pos += 1

                if cur_node.end:
                    min_extra = min(min_extra, dfs(cur_pos))

            return min_extra


        return dfs(0)