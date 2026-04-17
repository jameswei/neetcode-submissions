class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        break_into_words = [False] * len(s)
        break_into_words[0] = s[0] in wordDict

        for i in range(1, len(break_into_words)):
            if s[i] in wordDict:
                break_into_words[i] = True
            elif s[0:i+1] in wordDict:
                break_into_words[i] = True
            else:
                # find previous breakable positions
                j = i - 1
                while j >= 0:
                    if break_into_words[j] and s[j+1:i+1] in wordDict:
                        break_into_words[i] = True
                        break
                    j -= 1
                

            print("matrix:", break_into_words)
        
        return break_into_words[-1]
            