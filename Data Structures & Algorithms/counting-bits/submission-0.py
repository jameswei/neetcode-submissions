class Solution:
    def countBits(self, n: int) -> List[int]:
        num_of_one_in_bits = []

        for i in range(n+1):
            
            flag = 0b1
            count = 0

            for j in range(i):
                mask = flag << j
                if mask & i == mask:
                    count += 1
            print(f"num: {i}, num of 1 in bits: {count}")
            num_of_one_in_bits.append(count)

        return num_of_one_in_bits
