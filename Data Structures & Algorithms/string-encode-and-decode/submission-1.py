class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        encoded = ""
        length_part = []
        content_part = ""

        for cur_str in strs:
            length_part.append(len(cur_str))
            content_part += cur_str
        
        encoded += ','.join(str(x) for x in length_part)
        encoded += '分' 
        encoded += content_part
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if str == "":
            return []
        separated = s.split("分")
        length_part, content_part = separated[0], separated[1]

        decoded = []
        lengths = length_part.split(",")
        start = 0
        for length in lengths:
            l = int(length)
            decoded.append(content_part[start: start + l])
            start += l

        return decoded        
