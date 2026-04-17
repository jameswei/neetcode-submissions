class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # 将所有单词放入集合，包括起始单词
        word_set = set(wordList)
        word_set.add(beginWord)
        
        # 构建模式字典
        pattern_dict = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_dict[pattern].append(word)
        
        # BFS初始化
        queue = deque([beginWord])
        visited = {beginWord}
        distance = 1  # 起始单词算第一步
        
        while queue:
            # 处理当前层的所有单词
            for _ in range(len(queue)):
                current_word = queue.popleft()
                
                # 如果找到终点，返回距离
                if current_word == endWord:
                    return distance
                
                # 生成当前单词的所有模式，并找到邻居
                for i in range(len(current_word)):
                    pattern = current_word[:i] + '*' + current_word[i+1:]
                    
                    # 遍历该模式下的所有单词
                    for neighbor in pattern_dict[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            
            distance += 1
        
        return 0