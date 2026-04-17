class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 本质就是在无向图里找最短路径

        total_words = set(wordList)
        if endWord not in total_words:
            return 0
        
        total_word_count = len(total_words)

        # 建图
        # 遍历word_list，为每个word生成pattern，按照pattern进行分组
        # 最终就用这个模式表来当作图，而不用再转成邻接表形式
        pattern_groups = defaultdict(set)
        for word in total_words:
            
            for j in range(len(word)):
                pattern = word[:j]+'*'+word[j+1:]
                pattern_groups[pattern].add(word)
        

        # bfs
        queue = deque()
        for i in range(len(beginWord)):
            pattern = beginWord[:i]+'*'+beginWord[i+1:]
            if pattern not in pattern_groups:
                continue
            queue.append(pattern)

        distance = 1
        visited_words = {beginWord}
        while len(queue) > 0:

            for _ in range(len(queue)):
                pattern = queue.popleft()
                matched_words = pattern_groups[pattern]
                
                for word in matched_words:
                    if word == endWord:
                        return distance+1

                    if word in visited_words:
                        continue
                    
                    visited_words.add(word)
                    for k in range(len(word)):
                        p = word[:k]+'*'+word[k+1:]
                        if len(pattern_groups[p]) > 0:
                            queue.append(p)

            distance += 1


        return 0
