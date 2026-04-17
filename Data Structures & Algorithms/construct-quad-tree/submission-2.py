"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # val = True if grid==1 else False
        # val = True or False if isLeaf == False

        # n*n 矩阵，n 是偶数
        n = len(grid)

        if n == 1:
            # 1*1单个元素，只能是个叶子节点
            return Node(grid[0][0]==1, True)

        # i,j是左上角的起点，size是大小，每次递归时/2，最小是2^0==1
        def dfs(i: int, j: int, size: int) -> Node:
            if size == 1:
                return Node(grid[i][j]==1, True)
            
            # divide to small grid
            quotient = size // 2

            top_left = dfs(i, j, quotient)
            top_right = dfs(i, j+quotient, quotient)
            bottom_left = dfs(i+quotient, j, quotient)
            bottom_right = dfs(i+quotient, j+quotient, quotient)


            # 只有都是叶子节点才合并
            if (top_left.isLeaf and 
                top_right.isLeaf and 
                bottom_left.isLeaf and 
                bottom_right.isLeaf and 
                top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True)

            # 创建父节点
            return Node(False, False, top_left, top_right, bottom_left, bottom_right)


        return dfs(0, 0, n)