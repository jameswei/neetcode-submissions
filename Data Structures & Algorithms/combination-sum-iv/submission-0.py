class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums中没有重复数字，题目名字虽然叫combination，看起来是组合问题
        # 但从题目示例中发现：1.可以重复选择，2.顺序不同就算不同
        # 所以这道题本质是permutation，也就是排列问题

        nums.sort()
        memo = [-1] * (target+1)

        # 记忆化+dfs
        def dfs(remaining: int) -> int:
            if remaining == 0:
                return 1

            if memo[remaining] != -1:
                return memo[remaining]

            num_of_comb = 0

            for i in range(len(nums)):
                num = nums[i]

                if num > remaining:
                    break
                
                num_of_comb += dfs(remaining-num)
            
            memo[remaining] = num_of_comb
            return num_of_comb

        return dfs(target)