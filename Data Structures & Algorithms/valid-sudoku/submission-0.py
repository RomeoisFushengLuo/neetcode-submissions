class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_sets = [set() for _ in range(len(board))]
        cols_sets = [set() for _ in range(len(board[0]))]
        sub_sets = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                cur_val = board[i][j]
                if (cur_val != ".") and (cur_val in rows_sets[i] or cur_val in cols_sets[j] or cur_val in sub_sets[3*(i//3)+j//3]):
                    return False
                else:
                    rows_sets[i].add(cur_val)
                    cols_sets[j].add(cur_val)
                    sub_sets[3*(i//3)+j//3].add(cur_val)

        return True
        