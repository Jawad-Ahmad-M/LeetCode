class Solution:

    def get_bit(self, no, index):
        return (no & (1 << index)) != 0

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [0] * 9
        columns = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue

                val = int(board[row][col]) - 1

                square = (row // 3) * 3 + (col // 3)

                if (self.get_bit(rows[row], val)
                    or self.get_bit(columns[col], val)
                    or self.get_bit(squares[square], val)):
                    return False

                rows[row] |= (1 << val)
                columns[col] |= (1 << val)
                squares[square] |= (1 << val)

        return True