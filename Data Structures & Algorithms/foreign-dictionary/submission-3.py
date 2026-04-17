class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        
        # 先后次序可以用有向图来表达，
        # 节点就是字符，边的方向就是顺序
        # 比如，t->f，表示f 在t 字符后面

        # 此题用邻接表表示图
        # 同时收集所有出现的字符
        # 收集每个字符的入度（被依赖的次数）
        
        all_chars = set()
        graph = {}
        in_degree = {}

        for word in words:
            for c in word:
                all_chars.add(c)

                if c not in graph:
                    graph[c] = []

                if c not in in_degree:
                    in_degree[c] = 0

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
                # if word_a[j] not in graph:
                #     graph[word_a[j]] = []
                graph[word_a[j]].append(word_b[j])
                in_degree[word_b[j]] += 1

            # no difference but word_a is longer than word_b
            # for example: wrtkj and wrt,
            # it's invalid lexicongraphical order
            elif j < len(word_a):
                return ""

        print(f"all_chars: {all_chars}")
        print(f"graph: {graph}")
        print(f"in_degree: {in_degree}")

        # graph is built, let's traverse it in BFS
        # Kahn algorithm
        """
        初始化一个队列，把所有入度为 0 的字母加入队列。
        初始化结果列表 order = []。
        当队列不为空：
        弹出队首字母 u，加入 order。
        遍历 u 的所有邻居 v（即 graph[u] 中的每个字母）：
        将 v 的入度减 1。
        如果 v 的入度变为 0，把 v 加入队列。
        结束后，如果 order 的长度等于所有字母的数量，说明排序成功（无环），返回 order 连接成的字符串。
        否则，说明有环，返回 ""。
        """
        order = list()
        def bfs():
            queue = deque()
            for k in in_degree:
                # no other chars prior to this char
                if in_degree[k] == 0:
                    queue.append(k)
            
            while len(queue) > 0:
                u = queue.popleft()
                order.append(u)

                for v in graph[u]:
                    in_degree[v] -= 1

                    if in_degree[v] == 0:
                        queue.append(v)
        
        bfs()
        
        if len(order) == len(all_chars):
            return "".join(order)
        return ""