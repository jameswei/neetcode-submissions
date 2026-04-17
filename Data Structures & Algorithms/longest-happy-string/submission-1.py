class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = []
        if a > 0:
            heapq.heappush(chars, (-1*a, 'a'))
        if b > 0:
            heapq.heappush(chars, (-1*b, 'b'))
        if c > 0:
            heapq.heappush(chars, (-1*c, 'c'))

        print(f"chars: {chars}")

        # 允许相邻字符相同，但连续相同字符不能超过2个
        # 使用2次后需要等待
        waiting_char = None
        res = []
        while len(chars) > 0:
            cnt, char = heapq.heappop(chars)
            
            if len(res) > 0 and char == res[-1]:
                res.append(char)
                cnt += 1

                if waiting_char is not None:
                    heapq.heappush(chars, waiting_char)
                    waiting_char = None

                if cnt < 0:
                    waiting_char = (cnt, char)

            else:
                res.append(char)
                cnt += 1

                if waiting_char is not None:
                    heapq.heappush(chars, waiting_char)
                    # 放回去了后就要清空等待区
                    waiting_char = None

                if cnt < 0:
                    heapq.heappush(chars, (cnt, char))

        return ''.join(res)