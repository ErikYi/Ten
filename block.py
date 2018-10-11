class Block:

    def __init__(self, n_player=2):
        self._n_player = n_player
        self.owner = None
        self.owned_cells = [set() for x in xrange(n_player)]
        print self.owned_cells

    def put(self, player, cell):
        self.owned_cells[player].add(cell)
        self.check_win()

    def check_win(self):
        for p, cells in enumerate(self.owned_cells):
            if self._check_player_win(cells):
                self.owner = p
                break

    def _check_player_win(self, owned):
        # always check from smaller index to greater
        for cell in [0, 1, 2, 3, 6]:
            if cell in owned:
                if self._check_win_cells(cell, owned):
                    return True
        return False

    def _check_win_cells(self, cell, owned):
        """
        only check winning cells having greater indexes, because those with smaller indexes should be checked earlier
        """
        if cell == 0:
            return (1 in owned and 2 in owned) or (3 in owned and 6 in owned) or (4 in owned and 8 in owned)
        if cell == 1:
            return 4 in owned and 7 in owned
        if cell == 2:
            return (4 in owned and 6 in owned) or (5 in owned and 8 in owned)
        if cell == 3:
            return 4 in owned and 5 in owned
        return 6 in owned and 7 in owned and 8 in owned

    def to_string_array(self):
        string_array = []  # contains three strings, each represents 1 row
        if self.owner is not None:
            print_board = [[str(self.owner) for y in xrange(3)] for x in xrange(3)]
        else:
            print_board = [['.' for y in xrange(3)] for x in xrange(3)]
            for idx, cells in enumerate(self.owned_cells):
                for c in cells:
                    print_board[c/3][c%3] = str(idx)
            
        for row in print_board:
            string_array.append(' '.join(row))
        return string_array
