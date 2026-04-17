class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 本质就是在无向图里找最短路径
        # 按wordlist建图，节点是word，边是一个差异字符
        # 再将begin和end也纳入图，如果begin或end没有边，那就无解

        # 建图
        # 遍历建的话需要 n*n*l, n=len(wordlist)+begin+end, l=len(word)
        if endWord not in set(wordList):
            return 0
        
        word_transform = defaultdict(list)
        total_words = [beginWord] + wordList
        total_word_count = len(total_words)

        
        for i in range(len(total_words)):
            for j in range(i+1, len(total_words)):
                source_word = total_words[i]
                target_word = total_words[j]

                diff = 0
                u, v = 0, 0
                while diff < 2 and u < len(source_word) and v < len(target_word):
                    if source_word[u] != target_word[v]:
                        diff += 1
                    
                    u += 1
                    v += 1

                # 因为没有相同的单词，所以只能是 diff>=1
                if diff == 1:
                    # 无向图，两边都加关系
                    word_transform[source_word].append(target_word)
                    word_transform[target_word].append(source_word)

        if len(word_transform[beginWord]) == 0 or len(word_transform[endWord]) == 0:
            return 0

        shortest_distance = 2**31-1

        def dfs(word: str, path: list[str], visited: set[str]):
            nonlocal shortest_distance
            # 找到了，更新结果
            if word == endWord:
                print(f"transform: {path}")
                shortest_distance = min(shortest_distance, len(path))
                return         

            target_words = word_transform[word]
            # 无路可走
            if len(target_words) == 0:
                return

            for target_word in target_words:
                # 不走回头路
                if target_word not in visited:
                    visited.add(target_word)
                    path.append(target_word)

                    dfs(target_word, path, visited)

                    visited.remove(target_word)
                    path.pop()

        dfs(beginWord, [beginWord], set())

        return 0 if shortest_distance == 2**31-1 else shortest_distance
