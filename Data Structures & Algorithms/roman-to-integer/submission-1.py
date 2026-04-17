class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # 'I'放在'V'和'X'前面当作减法，放在后面当作加法
        # 'X'放在'L'和'C'前面当作减法，放在后面当作加法
        # 'C'放在'D'和'M'前面当作减法，放在后面当作加法
        special_numerals = {'I':['V','X'],'X':['L','C'],'C':['D','M']}

        res = 0
        prev_char = ''
        for i in range(len(s)-1, -1, -1):
            cur_char = s[i]
            num = roman_numerals[cur_char]
            
            if cur_char in special_numerals.keys() and prev_char in special_numerals[cur_char]:
                num *= -1

            res += num
            prev_char = cur_char

        return res
