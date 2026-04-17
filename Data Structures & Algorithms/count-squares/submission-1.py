class CountSquares:

    def __init__(self):
        self._point_to_count = defaultdict(int)
        self._max_x = 0
        self._max_y = 0

    def add(self, point: List[int]) -> None:
        self._point_to_count[(point[0],point[1])] += 1

        self._max_x = max(point[0], self._max_x)
        self._max_y = max(point[1], self._max_y)
        

    def count(self, point: List[int]) -> int:
        total_count = 0
        x, y = point[0], point[1]
        
        movement_on_diagonal = [[-1,1], [1,-1], [1,1],[-1,-1]]
        for dx, dy in movement_on_diagonal:
            nx, ny = x, y
            while 0<=nx+dx<=self._max_x and 0<=ny+dy<=self._max_y:
                nx, ny = nx+dx, ny+dy
                if self._point_to_count[(nx,ny)] == 0:
                    continue

                total_count += self._point_to_count[(nx,ny)] * self._point_to_count[(x,ny)] * self._point_to_count[(nx,y)]
        
        return total_count
