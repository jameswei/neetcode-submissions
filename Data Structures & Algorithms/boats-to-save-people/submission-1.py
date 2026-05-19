class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weight_count = defaultdict(int)
        
        for w in people:
            weight_count[w] += 1

        min_num = 0
        for l in range(limit, 0, -1):
            if weight_count[l] == 0:
                continue
            
            elif weight_count[limit-l] > 0:
                if weight_count[l] >= weight_count[limit-l]:
                    weight_count[limit-l] = 0
                else:
                    weight_count[limit-l] -= weight_count[l]
                    
            min_num += weight_count[l]
            weight_count[l] = 0

        
        return min_num