class Solution:
    def checkValidString(self, s: str) -> bool:
        # 分别从乐观和悲观的角度来计算未关闭的左括号'('
        # 因为有通配符'*'存在，它既可以当作'('，也可以当作')'，还能当作''。
        # 所以乐观的想法下，认为之后还有')'存在，可以把通配符继续当作'('
        # 而悲观的想法下，认为之后可能没有')'存在了，必须把通配符当作')'，尽早关闭前面的'('
        optimistic = 0
        pessimistic = 0
        star_count = 0

        for char in s:
            if char == "(":
                pessimistic += 1
                optimistic += 1
            elif char == ")":
                pessimistic -= 1
                optimistic -= 1
            # char == "*"
            else:
                star_count += 1
                optimistic += 1
                pessimistic -= 1

            # 如果没有出现过通配符'*'，那无论乐观还是悲观，它们都应该准确反映当前括号匹配的情况
            # 因为对于'('或')'，这样“明确的毫无争议的事实”，无论乐观还是悲观，都应该如实体现！
            # 而二者值不相等时，说明出现过通配符'*'，所以才会有乐观的做法和悲观的做法
            if optimistic != pessimistic:
                # 如果乐观的做法下，当前左括号少于右括号，（相当于未关闭的右括号数量）
                # 那肯定没法是合法的括号对儿
                if optimistic < 0:
                    return False
                
                # 如果悲观的做法下，当前左括号少于右括号，那可能是之前的操作时过于悲观，
                # 可以取折中，把通配符当作''来处理
                if pessimistic < 0:
                    while pessimistic != 0 and star_count > 0:
                        pessimistic += 1
                    # pessimistic = max(0, pessimistic)

        return pessimistic == 0