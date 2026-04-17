class TrieTreeNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode()
    
    def insert(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieTreeNode()
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
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 要求分割后所有子串都是word

        # 先根据字典先构造前缀树
        trie = TrieTree()

        for word in wordDict:
            trie.insert(word)

        # 遍历字符串s的每个字符，从字典树匹配前缀
        # 错误思路：
        # 如果s[i...j]构成单词，可以选择分割，继续匹配s[j+1:]；也可以不分割

        n = len(s)
        sentences = []

        def dfs(i: int, words: list[str]):
            if i == n:
                sentences.append(" ".join(words))
                return
            
            # 正确思路：
            # 对于当前起点i，应该把结束位置j定在哪里以形成一个新单词？
            # 这个位置可以是[i...n-1]，所以需要循环来枚举所有可能的i
            for j in range(i, n):
                content = s[i:j+1]
                if trie.is_a_word(content):
                    # 选择
                    words.append(content)
                    dfs(j+1, words)
                    # 撤销选择，此时words中不包含[i:j]
                    words.pop()

                    # 而不选择的方式是由for循环隐式完成了，
                    # 也就是pop()后，j继续移动，words中不包含刚才的选择


            return

        dfs(0, [])
        return sentences