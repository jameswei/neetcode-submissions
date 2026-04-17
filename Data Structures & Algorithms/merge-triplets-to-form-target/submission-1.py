class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # target 每个位置的值，必须存在于某个triplet的对应位置上，否则无解
        # 如果某个 triplet 的某个位置的值 大于 target 对应位置的值，
        # 那么这个 triplet 绝对不能选

        base_triplet = [0] * len(target)

        for triplet in triplets:
            matched = True
            for i in range(len(target)):
                if triplet[i] > target[i]:
                    matched = False
                    break
            if matched:
                for j in range(len(base_triplet)):
                    base_triplet[j] = max(base_triplet[j], triplet[j])

        return base_triplet == target