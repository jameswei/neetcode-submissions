class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        longest_len = 1

        # longest_subseq[i] = length of longest subsequence ended with nums[i]
        # default longest length is 1 as a subsequence with single char
        longest_subseq = [1] * len(nums)
        # dp[i] = max(dp[i], dp[j]+1) for each j<i and nums[j]<nums[i]

        for i in range(1, len(longest_subseq)):

            for j in range(0, i):

                if nums[j] >= nums[i]:
                    continue
                
                longest_subseq[i] = max(longest_subseq[i], longest_subseq[j]+1)

            longest_len = max(longest_len, longest_subseq[i])

        return longest_len