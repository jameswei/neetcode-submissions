class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 类似于 2sum 的变体，个数不超过 2 个，和不超过 limit
        
        # 排序，获得单调递增
        people.sort()

        i, j = 0, len(people)-1
        min_num = 0

        while i < j:
            w_1, w_2 = people[i], people[j]
            if w_1 + w_2 <= limit:
                min_num += 1
                i += 1
                j -= 1
            elif w_2 <= limit:
                min_num += 1
                j -= 1
        
        # i==j:
        if i == j and people[j] <= limit:
            min_num += 1

        return min_num
        