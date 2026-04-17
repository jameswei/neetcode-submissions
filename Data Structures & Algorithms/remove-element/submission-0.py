class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 不能排序
        # nums.sort()
        removed_elements = []

        for n in nums:
            if n == val:
                continue
            removed_elements.append(n)
        
        for i in range(len(removed_elements)):
            nums[i] = removed_elements[i]

        return len(removed_elements)