# ["hrn","hrf","er","enn","rfnn"]
# "hernf"

# ["wrt", "wrf", "er", "ett", "rftt"]
# [""]

# words=["wrtkj","wrt"]
# invalid
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 先后次序可以用有向图来表达，
        # 节点就是字符，边的方向就是顺序
        return ""