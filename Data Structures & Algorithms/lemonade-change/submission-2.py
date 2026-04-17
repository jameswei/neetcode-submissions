class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 这个解法更能反映“贪心”的思想
        # 本质上是先更新，再检查合法性

        # 计数
        five_bill, ten_bill = 0, 0

        for bill in bills:
            if bill == 5:
                five_bill += 1
            
            elif bill == 10:
                five_bill -= 1
                ten_bill += 1

            elif bill == 20 and ten_bill > 0:
                ten_bill -= 1
                five_bill -= 1
            
            else:
                five_bill -= 3

            if five_bill < 0:
                return False

        return True