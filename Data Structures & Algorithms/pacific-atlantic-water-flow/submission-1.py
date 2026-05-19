class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        flow_into_pacific = set()
        flow_into_atlantic = set()

        CELLS_BEYOND_PACIFIC = list()
        CELLS_BEYOND_ATLANTIC = list()

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i == 0 or j == 0:
                    CELLS_BEYOND_PACIFIC.append((i, j))
                if i == len(heights)-1 or j == len(heights[i])-1:
                    CELLS_BEYOND_ATLANTIC.append((i,j))
        
        print(CELLS_BEYOND_ATLANTIC)
        print(CELLS_BEYOND_PACIFIC)

        def dfs(heights: List[List[int]], coordinates: tuple[int, int], cells: Set, explored: Set):
            if coordinates in explored:
                return

            x, y = coordinates[0], coordinates[1]
            cur_height = heights[x][y]
            explored.add(coordinates)

            can_flow = (x-1 >= 0 and heights[x-1][y] >= cur_height) or (x+1 <= len(heights) and heights[x+1][y] >= cur_height) or (y-1 >= 0 and heights[x][y-1] >= cur_height) or (y+1 <= len(heights[x])-1 and heights[x][y+1] >= cur_height)
            if not can_flow:
                cells.add(coordinates)
                return

            if x-1 >= 0 and heights[x-1][y] >= cur_height:
                dfs(heights, (x-1, y), cells, explored)
            if x+1 <= len(heights)-1 and heights[x+1][y] >= cur_height:
                dfs(heights, (x+1, y), cells, explored)
            if y-1 >= 0 and heights[x][y-1] >= cur_height:
                dfs(heights, (x, y-1), cells, explored)
            if y+1 <= len(heights[x])-1 and heights[x][y+1] >= cur_height:
                dfs(heights, (x, y+1), cells, explored)
            
            cells.add(coordinates)



        explored_for_pacific = set()
        for coordinates in CELLS_BEYOND_PACIFIC:
            dfs(heights, coordinates, flow_into_pacific, explored_for_pacific)

        explored_for_atlantic = set()
        for coordinates in CELLS_BEYOND_ATLANTIC:
            dfs(heights, coordinates, flow_into_atlantic, explored_for_atlantic)

        
        flow_into_both_oceans = flow_into_atlantic & flow_into_pacific

        return [list(x) for x in flow_into_both_oceans]