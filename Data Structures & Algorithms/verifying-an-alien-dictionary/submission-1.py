class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 原始的内容是个小写字母的permutation（也就是某种乱序排列），感觉是bfs拓扑排序
        # 错！拓扑排序主要用于找一种“有效顺序”，这个题目已经给定一个顺序，只是验证它是否有效
        
        # 更正确的想法是：如果给定的order是有效的，那么按照这样order对words排序，会得到一致的结果。
        # 所以进一步，应该想办法通过order这个字母表建立个排序顺序，然后再用这个排序顺序作为排序器去排序words。
        # 自定义comparator的实现时，通常都转化成算数减-，根据结果正负来判断顺序
        n = len(words)
        m = len(order)

        char_to_pos = {}
        for i in range(m):
            # order是字母表，所以不会有重复字符
            char = order[i]
            char_to_pos[char] = i
        
        def word_rank(word: str) -> list[int]:
            return [char_to_pos[char] for char in word]

        return words == sorted(words, key=word_rank)