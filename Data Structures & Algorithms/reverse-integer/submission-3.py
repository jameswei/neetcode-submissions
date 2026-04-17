class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        as_str = str(x)
        negative = as_str[0] == '-'
        length = len(as_str) if not negative else len(as_str)-1

        min_val = -2**31
        max_val = 2**31-1

        zero_count = 0
        for i in range(len(as_str)-1, ((1 if negative else 0)-1), -1):
            if as_str[i] == '0':
                zero_count += 1
            else:
                break
        
        # lowest_pos is lowest non-zero pos
        lowest_pos = -1-zero_count

        lowest_val = int(as_str[lowest_pos])
        highest_val = (-1 if negative else 1) * lowest_val * (10 ** (length-1-zero_count))


        if highest_val > max_val or highest_val < min_val:
            return 0

        res = ["-"] if negative else []

        for i in range(len(as_str)+lowest_pos, ((1 if negative else 0)-1), -1):
            d = as_str[i]
            res.append(d)

        reversed_str = ''.join(res)
        return int(reversed_str)
