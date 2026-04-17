class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_dict = set(wordDict)
        word_len_set = set(len(word) for word in word_dict)

        # [0,i] == breakable into words
        # s[0:i+1]
        word_breakable = [False] * len(s)
        # s[0:1]
        word_breakable[0] = s[0] in word_dict

        for i in range(1, len(s)):
            for l in word_len_set:
                j = i - l + 1

                if j < 0:
                    continue
                    
                if s[j:i+1] not in word_dict:
                    continue
                
                if j - 1 < 0:
                    word_breakable[i] = True
                else:
                    word_breakable[i] = word_breakable[j-1]

                if word_breakable[i]:
                    break

            
        return word_breakable[-1]


            