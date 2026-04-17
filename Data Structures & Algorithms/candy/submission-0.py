class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 符合条件的最少数量
        # 分解成两个方向来考虑：
        # 从左往右：如果右边孩子评分比左边高，右边孩子的糖数 = 左边孩子的糖数 + 1。
        # 从右往左：如果左边孩子评分比右边高，左边孩子的糖数 = 右边孩子的糖数 + 1。

        n = len(ratings)

        left_to_right = [0] * n

        left_to_right[0] = 1
        prev_rating = ratings[0]

        for i in range(1, n):
            if ratings[i] > prev_rating:
                left_to_right[i] = left_to_right[i-1] + 1
            else:
                left_to_right[i] = min(1, left_to_right[i-1])
        
            prev_rating = ratings[i]
        
        right_to_left = [0] * n
        right_to_left[n-1] = 1
        prev_rating = ratings[n-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > prev_rating:
                right_to_left[i] = right_to_left[i+1] + 1
            else:
                right_to_left[i] = min(1, right_to_left[i+1])
            
            prev_rating = ratings[i]

        total_candies = 0
        for i in range(n):
            total_candies += max(left_to_right[i], right_to_left[i])

        return total_candies
