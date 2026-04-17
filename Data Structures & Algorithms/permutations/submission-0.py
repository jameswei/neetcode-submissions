class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # unique integers
        # permutation 是找排列
        if len(nums) == 1:
            return [nums]

        res = []

        def dfs(options: list[int], path: list[int]):
            if len(options) == 0:
                res.append(path[:])
                return

            for i in range(len(options)):
                path.append(options[i])
                new_options = []
                if i == 0:
                    new_options.extend(options[1:])
                elif i == len(options)-1:
                    new_options.extend(options[:len(options)-1])
                else:
                    new_options.extend(options[:i])
                    new_options.extend(options[i+1:])

                dfs(new_options, path)

                path.pop()

        dfs(nums, [])
        return res