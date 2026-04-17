class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = defaultdict(int)

        for i in range(len(s)):
            last_occurrence[s[i]] = i

        print(f"last_occurrence: {last_occurrence}")

        begin, end = 0, 0
        pos = 0
        res = []

        while begin < len(s):
            pos = begin
            while end <= pos and end < len(s):
                end += 1
                new_char = s[end-1]
                new_pos = last_occurrence[new_char]
                print(f"char: {new_char}, last_occurrence: {new_pos}")
                
                if new_pos > pos:
                    pos = new_pos
            
            # r == pos+1 or r == len(s)
            # len = r-1-l+1
            res.append(end - begin)
            begin = end

        return res