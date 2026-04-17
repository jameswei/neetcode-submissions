class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 分成k个非空subarray，使得最大的和尽可能小
        # [2,4,10,1,5]分两个subarray，可以分成
        # [2],[4,10,1,5]，最大的和是20
        # [2,4],[10,1,5]，最大的和是16
        # [2,4,10],[1,5]，最大的和是16
        # [2,4,10,1],[5]，最大的和是17 
        # 也就是分割k-1词，总共有len-1个位置

        if k == 1:
            return sum(nums)

        elif k == len(nums):
            return max(nums)

        n = len(nums)

        def can_split(m: int) -> bool:
            # 统计subarray的个数，而不是分割的次数
            subarray_count = 1
            cur_sum = 0
            for num in nums:
                # 单个就超过，肯定不行
                if num > m:
                    return False
                
                cur_sum += num

                # 必须分割
                if cur_sum > m:
                    subarray_count += 1
                    cur_sum = num
                    if subarray_count > k:
                        return False
            
            # 遍历完了
            return True

        min_subarr_sum = 2**31-1
        # 在最大的单个数和所有数的和之间以二分查找方式找最小的解
        l, r = max(nums), sum(nums)
        # [l,r]
        while l <= r:
            m = (l+r)//2

            ok = can_split(m)
            
            if ok:
                # 满足要求，更新结果，尝试减小
                min_subarr_sum = min(min_subarr_sum, m)
                r = m - 1
            else:
                l = m + 1

        return min_subarr_sum