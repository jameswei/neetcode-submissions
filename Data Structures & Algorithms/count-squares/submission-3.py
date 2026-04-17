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

        for p in list(self._point_to_count):
            px, py = p[0], p[1]
            if x == px or y == py:
                continue
            # on main or anti diagonal
            if abs(x-px) == abs(y-py):
                total_count += self._point_to_count[(px,py)] * self._point_to_count[(x,py)] * self._point_to_count[(px,y)]
        
        return total_count
