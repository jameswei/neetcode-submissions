class Solution:
    def reorganizeString(self, s: str) -> str:
        # 既然s由英文字母构成，根据ord('char')可以得到确定的ascii字符值
        n = len(s)

        # 字符个数
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1

        max_count = max(char_count.values())
        if max_count > (n+1)//2:
            return ""

        res = []

        # 等待队列，但其实最多只会有1个字符在等待
        # 因为每一轮只从堆中弹出一个字符来用，用完后为了避免相邻字符是重复的，所以将它放入等待。
        # 下一轮从堆中弹出另一个字符来用后，等待中的字符就“复活了”，可以重新放回堆中
        waiting_char = None

        # (remaining_count:char)堆
        available_chars = []
        for k, v in char_count.items():
            heapq.heappush(available_chars, (-1*v, k))
        
        while len(available_chars) > 0:
            # 从堆中弹出时，cnt是负值
            cnt, cur_char = heapq.heappop(available_chars)
            res.append(cur_char)

            if waiting_char is not None:
                heapq.heappush(available_chars, waiting_char)
            
            # 因为cnt是负值的数量，所以数量-1在这里变成+1，判断时也要变成<0
            cnt += 1
            # 还没使用完，放入等待
            waiting_char = (cnt, cur_char) if cnt < 0 else None

        # if waiting_char is not None:
        #     if waiting_char[0] == 1:
        #         res.append(waiting_char[1])
        #     else:
        #         return ""
        
        return ''.join(res)