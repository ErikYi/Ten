from block import Block


class TenBoard:
    P1 = 0
    P2 = 1
    PLAYERS = ['P1', 'P2']

    def __init__(self):
        self.blocks = [Block() for x in range(9)]
        self.owned_blocks = [set(), set()]  # [p1_owned, p2_owned]

    def put(self, p, i, j):
        self.blocks[i].put(p, j)
        self.update_owner()
        self.print_board()
        return self.check_win()

    def update_owner(self):
        for i in range(9):
            if self.blocks[i].owner is not None:
                self.owned_blocks[self.blocks[i].owner].add(i)

    def check_win(self):

        for i in range(2):
            if self._check_player(self.owned_blocks[i]):
                return self.PLAYERS[i]
        return None

    def _check_player(self, owned):
        # always check from smaller index to greater
        for block in [0, 1, 2, 3, 6]:
            if block in owned:
                if self._check_win_blocks(block, owned):
                    return True

        return False

    def _check_win_blocks(self, block, owned):
        """
        only check winning blocks having greater indexes, because those with smaller indexes should be checked earlier
        """
        if block == 0:
            return (1 in owned and 2 in owned) or (3 in owned and 6 in owned) or (4 in owned and 8 in owned)
        if block == 1:
            return 4 in owned and 7 in owned
        if block == 2:
            return (4 in owned and 6 in owned) or (5 in owned and 8 in owned)
        if block == 3:
            return 4 in owned and 5 in owned
        return 6 in owned and 7 in owned and 8 in owned

    def print_board(self):

        board_string_array = []  # contains three strings, each represents 3 rows
        for i in range(3):
            block_string_array = []  # contains three strings, each represents 1 row
            block_cells = []
            for j in range(3):
                block_cells.append(self.blocks[3 * i + j].to_string_array())

            for k in range(3):
                block_string_array.append('|'.join([block_cells[0][k], block_cells[1][k], block_cells[2][k]]) + '\n')

            board_string_array.append(''.join(block_string_array))

        print '-----+-----+-----\n'.join(board_string_array)
