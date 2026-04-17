class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m, n = len(hand), groupSize
        if m % n != 0:
            return False
        
        counter = defaultdict(int)
        for num in hand:
            counter[num] += 1

        hand.sort()
        for i in range(m):
            num = hand[i]
            # 已经排序过，如果num没有了，
            # 要么其他组用掉了，要么整个[..num]都已经没有了
            if counter[num] == 0:
                continue
            
            # 一定是分到新组的
            counter[num] -= 1
            for k in range(n-1):
                # 没有 num+k+1 ，那就分不了组
                if counter[num+k+1] == 0:
                    return False
                # 能分，就用掉一张
                counter[num+k+1] -= 1

        return True
            
