class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_counter = defaultdict(int)

        for c in hand:
            card_counter[c] += 1

        card_heap = list(card_counter.keys())
        heapq.heapify(card_heap)
        queue = deque()

        while len(card_heap) > 0:
            first_card = heapq.heappop(card_heap)
            card_counter[first_card] -= 1
            if card_counter[first_card] > 0:
                queue.append(first_card)

            if len(card_heap) == 0:
                return False
            
            for k in range(groupSize-1):
                card = heapq.heappop(card_heap)
                if card != first_card+k+1:
                    return False
                card_counter[card] -= 1
                if card_counter[card] > 0:
                    queue.append(card)
            
            while len(queue) > 0:
                heapq.heappush(card_heap, queue.popleft())

        return True
            
            
                
                


            