class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = nums[n-k:]
        print(f"temp: {temp}")
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        print(f"nums: {nums}")
        for j in range(k):
            nums[j] = temp[j]
        
        return