class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 排序法很巧妙！
        # 把题目要求的要比较的信息融入进了排序过程，最后对排序结果取前k个

        return sorted(
                sorted(arr, key=lambda num: (abs(num-x),num))[:k]
            )