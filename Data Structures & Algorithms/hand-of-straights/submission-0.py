class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 排序后，保证相同值聚集在一起
        hand.sort()

        if groupSize * 2 != len(hand):
            return False

        groups = [[] for _ in range(2)]

        for i in range(len(hand)):
            num = hand[i]

            arranged = False
            for group in groups:
                if len(group) == 0 or (len(group)<groupSize and group[-1]+1==num):
                    group.append(num)
                    arranged = True
                    break
            
            if not arranged:
                print(f"num: {num} is not arranged")
                print(f"groups: {groups}")
                return False

        return True