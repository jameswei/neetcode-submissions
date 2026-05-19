class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1 = num1[::-1]
        num_2 = num2[::-1]
        
        res = [0] * (len(num_1)+len(num_2))
        
        for i in range(len(num_1)):
            num_a = int(num_1[i])
            for j in range(len(num_2)):
                num_b = int(num_2[j])

                val = num_a*num_b+res[i+j]

                res[i+j] = val % 10
                res[i+j+1] += val // 10

        res_str = []
        for k in res[::-1]:
            if k == 0:
                continue
            res_str.append(str(k))

        return ''.join(res_str)