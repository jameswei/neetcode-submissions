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
        # 比如，t->f，表示f 在t 字符后面

        # 图可以用邻接矩阵，也可以用邻接表
        # 此题用邻接表更合适，因为矩阵不好表达字符值

        if len(words) == 1:
            return words[0]
        
        graph = {}

        for i in range(len(words)):
            if i+1 > len(words)-1:
                break

            # compare adjacent two words
            word_a, word_b = words[i], words[i+1]

            # find the first different char
            j = 0
            while j < len(word_a) and j < len(word_b) and word_a[j] == word_b[j]:
                j += 1
                
            if j < len(word_a) and j < len(word_b):
                if word_a[j] not in graph:
                    graph[word_a[j]] = []
                graph[word_a[j]].append(word_b[j])

            # no difference but word_a is longer than word_b
            # for example: wrtkj and wrt,
            # it's invalid lexicongraphical order
            elif j < len(word_a):
                return ""


        # graph is built, let's traverse
        print(f"graph: {graph}")
        

        def dfs(key: str, res: list[str]):
            if key in visited:
                return

            visited.add(key)
            res.append(key)

            if key not in graph:
                return

            if len(graph[key]) == 0:
                return

            for k in graph[key]:
                dfs(k, res)
        
        longest_res = list()
        for key in graph:
            visited = set()
            res = list()
            dfs(key, res)
            if len(res) > len(longest_res):
                longest_res = res

        return "".join(longest_res)