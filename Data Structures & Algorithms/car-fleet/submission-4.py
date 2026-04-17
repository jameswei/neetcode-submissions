class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1 and len(speed) == 1:
            return 1

        list_of_position_and_speed = []

        n = len(position)

        for i in range(n):
            pair = (position[i], speed[i])
            list_of_position_and_speed.append(pair)
        
        # sorted by position then speed
        list_of_position_and_speed.sort(key=lambda x: x[0], reverse=True)

        groups = 0
        prev_time_to_destination = float('-inf')
        for i in range(len(list_of_position_and_speed)):
            pos, speed = list_of_position_and_speed[i][0], list_of_position_and_speed[i][1]
            time_to_destination = (target-pos) / speed

            # cannot catch up prev car
            if time_to_destination > prev_time_to_destination:
                groups += 1
                prev_time_to_destination = time_to_destination
        
        return groups