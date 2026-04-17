class Solution:
    def decodeString(self, s: str) -> str:
        # "2[a3[b]]c"
        # bbb->abbbabbb->abbbabbbc

        LEFT_BRACKET = "["
        RIGHT_BRACKET = "]"

        stack = []

        for c in s:
            # 遇到"["，需要弹出确保k是一个数字整体
            if c == LEFT_BRACKET:
                content = []
                while len(stack) > 0 and len(stack[-1]) == 1 and 48 <= ord(stack[-1]) <= 57:
                    content.append(stack.pop())
                stack.append(''.join(content[::-1]))
                stack.append(c)

            # 遇到"]"，需要弹出直到凑成一个"k[encoded]"
            elif c == RIGHT_BRACKET:
                content = []
                while len(stack) > 0 and stack[-1] != LEFT_BRACKET:
                    content.append(stack.pop())
                # 弹出无用的"["
                stack.pop()
                # 再弹出重复次数
                count = int(stack.pop())
                # 按count重复重新入栈
                stack.append((''.join(content[::-1]))*count)
            
            else:
                stack.append(c)

        return ''.join(stack)
