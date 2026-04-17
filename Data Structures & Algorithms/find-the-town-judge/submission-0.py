class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 找出入度为n-1的节点，返回它的索引

        count = defaultdict(int)

        for i in range(len(trust)):
            a, b = trust[i][0], trust[i][1]
            count[b] += 1
            count[a] -= 1

        for k, v in count.items():
            if v == n-1:
                return k
        
        return -1