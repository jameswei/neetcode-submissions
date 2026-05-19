# Input: ["hrn","hrf","er","enn","rfnn"]
# Output: "hernf"
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        max_word_len = 100
        ordered_letters = list()
        included_letters = set()

        # words are sorted in lexicographically
        # char of words[i] is prior to another char at the same position
        for i in range(max_word_len):
            for word in words:
                len_of_word = len(word)
                if i > len_of_word-1:
                    # 没有对应字符
                    continue
                
                cur_char = word[i]
                if len(ordered_letters) > 0:
                    prev_char = ordered_letters[-1]
                    if cur_char == prev_char or cur_char in included_letters:
                        continue
                
                ordered_letters.append(cur_char)
                included_letters.add(cur_char)

        return ''.join(ordered_letters)