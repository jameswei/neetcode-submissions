class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        break_into_words = [False] * len(s)
        break_into_words[0] = s[0] in wordDict

        for i in range(1, len(break_into_words)):
            if s[0:i+1] in wordDict:
                print("s[0:i+1]", s[0:i+1])
                break_into_words[i] = True
            else:
                # find last breakable position
                j = i - 1
                while j >= 0 and (not break_into_words[j]):
                    j -= 1
                
                # break_into_words[j] == True or j==-1
                # check if [j+1:i+1] in word dict
                if j != -1:
                    break_into_words[i] = s[j+1:i+1] in wordDict

            print("matrix:", break_into_words)
        
        return break_into_words[-1]
            