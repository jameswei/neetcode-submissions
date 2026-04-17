class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        else:
            carry = 1
            for i in range(len(digits)-1, -1, -1):
                place = 0
                num = digits[i] + carry
                if num > 9:
                    carry = 1
                    place = num % 10
                else:
                    carry = 0
                    place = num
                
                digits[i] = place
            
            if carry > 0:
                return [carry] + digits

            return digits