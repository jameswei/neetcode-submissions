class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))

        res = []
        for i in range(len(words)):
            cur_word = words[i]
            for j in range(i+1, len(words)):
                other_word = words[j]

                p, q = 0, 0

                # prune if two words have same length but have different first character
                if len(cur_word) == len(other_word) and cur_word[p] != other_word[q]:
                    continue

                while p < len(cur_word) and q < len(other_word):
                    if cur_word[p] == other_word[q]:
                        p += 1
                    else:
                        # reset p if not matched
                        p = 0
                    q += 1
                 
                if p == len(cur_word):
                    res.append(cur_word)
                    break

        return res