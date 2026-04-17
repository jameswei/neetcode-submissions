class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # target 每个位置的值，必须存在于某个triplet的对应位置上，否则无解
        # 如果某个 triplet 的某个位置的值 大于 target 对应位置的值，
        # 那么这个 triplet 绝对不能选

        candidates = []

        for triplet in triplets:
            matched = True
            for i in range(len(target)):
                if triplet[i] > target[i]:
                    matched = False
                    break
            if matched:
                candidates.append(triplet)

        base_triplet = [0] * len(target)

        for candidate in candidates:
            for i in range(len(candidate)):
                base_triplet[i] = max(base_triplet[i], candidate[i])

        res = True        
        for i in range(len(base_triplet)):
            res = res and base_triplet[i] == target[i]
            if not res:
                return False
        
        return res


            
                