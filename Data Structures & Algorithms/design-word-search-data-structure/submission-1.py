class TreeNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.word = True

    # word may contain dots '.' where dots can be matched with any letter.
    def search(self, word: str) -> bool:
        
        def dfs(node: TreeNode, idx: int) -> bool:
            cur = node

            for i in range(idx, len(word)):
                c = word[i]

                # wildcard
                if c == ".":
                    for child in cur.children:
                        # last char
                        if i == len(word)-1:
                            return cur.children[child].word

                        if dfs(cur.children[child], i+1):
                            return True

                    return False
                
                else:
                    if c not in cur.children:
                        return False
                
                    cur = cur.children[c]

            return cur.word

        return dfs(self.root, 0)


        
        
        