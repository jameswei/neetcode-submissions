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
        # 如果s[i...j]构成单词，可以选择断开，继续匹配s[j+1:]；也可以不断开继续匹配

        n = len(s)
        sentences = []

        def dfs(i: int, words: list[str]):
            if i == n:
                sentences.append(" ".join(words))
                return
            
            for j in range(i, n):
                content = s[i:j+1]
                if trie.is_a_prefix(content):
                    if trie.is_a_word(content):
                        words.append(content)
                        dfs(j+1, words)
                        words.pop()

            return

        dfs(0, [])
        return sentences