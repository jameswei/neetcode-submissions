class PrefixTreeNode:

    def __init__(self):
        # dict has no more than 26 entries a-z
        self.children = {}
        # indicate whether it is a word ended here
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixTreeNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # 如果之前插入的是另一个 word 和此具有相同的 prefix，
        # 那么依然可以按字符搜索完毕，但不是搜索当前给定word的含义
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        