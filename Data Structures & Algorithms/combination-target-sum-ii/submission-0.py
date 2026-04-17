class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序，单调增，方便剪枝
        candidates.sort()
        res = []

        def dfs(i: int, path: list[int], total: int):
            if total == target:
                res.append(path[:])
                return
            
            if i > len(candidates)-1:
                return

            if candidates[i] > target-total:
                return

            # 这种情况下会产生“重复的 subset”
            # 因为candidates中包含重复的数字，
            # 做选择时尽管不会选择同一个数，但是会选到重复的数，进而形成一样的path
            # 如果这里先检查下是否曾选过同样大小的数
            # 会产生错误，因为它避免的是在一条路径中选择相同数值的数，但这一点是题目允许的
            # if len(path) == 0 and candidates[i] != path[-1]:
            # 而需要避免的是，不同递归选择下的path，包含了数值相同的数

            # select
            path.append(candidates[i])
            dfs(i+1, path, total+candidates[i])
            path.pop()

            # 避免不同path中包含了同样数值的数，
            # 需要在“不选择”的情况下，直接把相同数值的数都跳过
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1

            dfs(i+1, path, total)

        dfs(0, [], 0)
        return res