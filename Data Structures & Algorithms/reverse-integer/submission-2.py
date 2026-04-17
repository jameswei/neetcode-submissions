class Solution:
    def reverse(self, x: int) -> int:
        # '123'->'321', '-120'->'-21'

        if x == 0:
            return 0

        as_str = str(x)
        negative = as_str[0] == '-'
        length = len(as_str) if not negative else len(as_str)-1

        print(f"as_str: {as_str}, negative: {negative}, digi_length: {length}")

        # float inf or -inf cannot be converted to integer

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

        print(f"zero_count: {zero_count}, lowest_pos: {lowest_pos}, lowest_val: {lowest_val}, highest_val: {highest_val}")
        print(f"min_val: {str(min_val)}, max_val: {str(max_val)}")

        # 8000000000
        # 2147483647
        if highest_val > max_val or highest_val < min_val:
            return 0

        res = ["-"] if negative else []

        for i in range(len(as_str)-1, ((1 if negative else 0)-1), -1):
            d = as_str[i]
            res.append(d)

        reversed_str = ''.join(res)
        return int(reversed_str)
