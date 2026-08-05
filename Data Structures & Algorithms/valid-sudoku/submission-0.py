class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            res = list(filter((".").__ne__, row))
            if len(res) != len(set(res)):
                return False

        reversed_board = list(zip(*board))
        for col in reversed_board:
            res = list(filter((".").__ne__, col))
            if len(res) != len(set(res)):
                return False
        
        grids = []
        for r in range(0,9,3):
            for c in range(0,9,3):
                grid = []
                for i in range(3):
                    grid.extend(board[r + i][c:c + 3])
                grids.append(grid)

        for grid in grids:
            res = list(filter((".").__ne__, grid))
            if len(res) != len(set(res)):
                return False
        return True      

        