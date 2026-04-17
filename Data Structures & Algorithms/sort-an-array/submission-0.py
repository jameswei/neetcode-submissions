class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
                return nums
        
        def partition(l: int, r: int) -> int:
            i, j = l-1, r+1
            # k = l + (r-l)//2
            k = (l+r) // 2
            pivot = nums[k]

            while True:
                i += 1
                # 找>= pivot 的值
                while nums[i] < pivot:
                    i += 1

                j -= 1
                # 找<= pivot 的值
                while nums[j] > pivot:
                    j -= 1

                # i 是从左向右看第一个>= pivot 的位置
                # j 是从左向右看最后一个<= pivot 的位置
                # 所以[l,j]全是<= pivot，而[j+1,r]全是>= pivot
                if i >= j:
                    return j
                else:
                    nums[i], nums[j] = nums[j], nums[i]

        def quick_sort(l: int, r: int):
            if l >= r:
                return

            p = partition(l, r)

            quick_sort(l, p)
            quick_sort(p+1, r)
        
        
        
        quick_sort(0, len(nums)-1)
        return nums