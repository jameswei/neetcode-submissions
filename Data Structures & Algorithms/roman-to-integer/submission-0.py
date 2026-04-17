class Solution:
    def romanToInt(self, s: str) -> int:
        # 观察发现罗马数字符号的递进规则是“用前一个数*5, 用前一个数*2，反复此过程”
        # 最小符号‘I’表示1，最大符号‘M’表示1000，总共7个
        roman_numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        special_numberals = {'V','X','L','C','D','M'}

        # 'I'放在'V'和'X'前面当作减法，放在后面当作加法
        # 'X'放在'L'和'C'前面当作减法，放在后面当作加法
        # 'C'放在'D'和'M'前面当作减法，放在后面当作加法
        res = 0
        prev_char = ''
        for i in range(len(s)-1, -1, -1):
            cur_char = s[i]
            num = roman_numerals[cur_char]
            if cur_char == 'I' and (prev_char == 'V' or prev_char == 'X'):
                num *= -1
            
            if cur_char == 'X' and (prev_char == 'L' or prev_char == 'C'):
                num *= -1

            if cur_char == 'C' and (prev_char == 'D' or prev_char == 'M'):
                num *= -1

            res += num
            prev_char = cur_char

        return res
