class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 只要存在重叠的trip，其重叠trip的人数总和大于capacity，就失败
        # 排序优先级是from，to，passengers
        trips.sort(key=lambda x : (x[1], x[2], x[0]))
        n = len(trips)

        cur_passengers = 0
        prev_drop_off_pos = 0

        for i in range(n):
            (passengers, pick_up_pos, drop_off_pos) = trips[i]

            # 行程有重叠
            if pick_up_pos < prev_drop_off_pos:
                if cur_passengers+passengers > capacity:
                    return False
                cur_passengers += passengers
            
            # 上个行程的重点和这个行程起点重叠也没关系，因为乘客先下后上
            else:
                # 上个行程乘客都下车，这个行程乘客上车
                cur_passengers = passengers

            # 更新行程终点
            prev_drop_off_pos = drop_off_pos
        
        return True