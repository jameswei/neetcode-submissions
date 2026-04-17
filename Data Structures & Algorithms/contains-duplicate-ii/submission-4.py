class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # 窗口最大长度k+1，题目要求是给定元素k距离内的范围
        size = k+1
        
        # 记录当前窗口内的所有元素
        window = set()
        # [0,0) 左闭右开窗口
        i, j = 0, 0

        for j in range(n):
            # 扩大窗口，加入窗口的新元素就是[j]
            new_n = nums[j]

            # 检查窗口大小
            while j-i+1 > size:
                old_n = nums[i]
                window.remove(old_n)
                i += 1

            # 检查窗口内状态
            if new_n in window:
                return True

            # 更新窗口状态
            window.add(new_n)

        return False

