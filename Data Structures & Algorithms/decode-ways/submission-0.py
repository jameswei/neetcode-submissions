# only UPPER_CASE letters
# 'A' -> 1, ... 'Z' ->'26'
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1

        # [0] is dummy slot
        # [i] is s[0:i] ways to decode
        ways_to_decode = [0] * (len(s)+1)

        ways_to_decode[0] = 1
        ways_to_decode[1] = 1

        # [i] = [i-1]+1 if can be combined
        # [i] = [i-1] if can't be single

        # fill in the state from the second char
        for i in range(1, len(s)):
            # can be single
            if s[i] != '0':
                ways_to_decode[i+1] += ways_to_decode[i]
            # can be combined?
            if int('10') <= int(s[i-1:i+1]) <= int('26'):
                ways_to_decode[i+1] += ways_to_decode[i-1]
                
        return ways_to_decode[-1]