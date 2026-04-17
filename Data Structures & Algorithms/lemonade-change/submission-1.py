class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 因为要确保净交易额是$5，所以才会有找零（0,5,15）

        remaining = {5: 0, 10: 0, 20: 0}
        total_remaining = 0

        for incoming in bills:
            total_remaining += incoming
            remaining[incoming] += 1

            # need give back the change
            if incoming == 10:
                if total_remaining < 5 or remaining[5] < 1:
                    return False
                
                total_remaining -= 5
                remaining[5] -= 1

            elif incoming == 20:
                if total_remaining < 15:
                    return False

                total_remaining -= 15

                if remaining[10] > 0 and remaining[5] > 0:
                    remaining[10] -= 1
                    remaining[5] -= 1
                elif remaining[5] >= 3:
                    remaining[5] -= 3
                else:
                    return False

        return True
