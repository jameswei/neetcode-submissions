class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weight_count = defaultdict(int)
        max_weight = 0
        for w in people:
            weight_count[w] += 1
            max_weight = max(max_weight, w)

        min_num = 0

        # 
        for w in range(max_weight, 0, -1):
            if weight_count[w] == 0:
                continue
            
            diff = min(limit-w, w-1)

            while diff > 0 and weight_count[diff] > 0:
                boats = min(weight_count[diff], weight_count[w])
                min_num += boats
                weight_count[w] -= boats
                weight_count[diff] -= boats

                if weight_count[w] == 0:
                    break
                
                if weight_count[diff] == 0:
                    diff -= 1

            if weight_count[w] > 0:
                min_num += (weight_count[w]//2+weight_count[w]%2) if w <= limit//2 else weight_count[w]
                weight_count[w] = 0
        
        return min_num