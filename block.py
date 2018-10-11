class Block:

    def __init__(self):
        self.owner = None
        self.owned_cells = [set(), set()]

    def put(self, i, p):
        self.owned_cells[p].add(i)
        self.check_win()

    def check_win(self):

        for i in range(2):
            if self._check_player(self.owned_cells[i]):
                self.owner = i
                break

    def _check_player(self, owned):
        # always check from smaller index to greater
        for cell in [0,1,2,3,6]:
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

        cells = [[str(self.owner) for y in range(3)] for x in range(3)]
        string_array = []  # contains three strings, each represents 1 row

        if self.owner is None:
            for i in range(3):
                for j in range(3):
                    if 3*i+j in self.owned_cells[0]:
                        cells[i][j] = '0'
                    elif 3*i+j in self.owned_cells[1]:
                        cells[i][j] = '1'
                    else:
                        cells[i][j] = '.'
        for row in cells:
            string_array.append(' '.join(row))

        return string_array
