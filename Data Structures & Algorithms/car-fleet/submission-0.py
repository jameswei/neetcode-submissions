class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # cars can be a fleet:
        # 1.after t time(hours), they arrive at the same position.
        # 2.the position is <= destination.

        time_to_destination = defaultdict(list)

        for i in range(len(position)):
            time = (target-position[i])//speed[i]
            time_to_destination[time].append(i)

        return len(time_to_destination.keys())