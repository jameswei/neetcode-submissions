class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 排序后，保证相同值聚集在一起
        hand.sort()

        # 没法按 group_size 分组
        if len(hand) % groupSize != 0:
            return False

        groups = [[] for _ in range(len(hand)//groupSize)]

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