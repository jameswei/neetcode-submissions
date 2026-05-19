class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 原始的内容是个小写字母的permutation（也就是某种乱序排列）
        # 感觉是bfs拓扑排序，先来构建邻接表
        # ["dag","disk","dog"]
        # {"a":["i"],"i":["o"]}
        n = len(words)
        adj_map = defaultdict(list)

        for i in range(n-1):
            word_a = words[i]
            word_b = words[i+1]
            min_len = min(len(word_a), len(word_b))

            for j in range(min_len):
                if word_a[j] == word_b[j]:
                    continue
                adj_map[word_a[j]].append(word_b[j])
                break

        print(f"adj_map: {adj_map}")
