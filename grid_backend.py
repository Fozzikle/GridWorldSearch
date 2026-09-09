class GridBackEnd:
    def __init__(self, rows, cols):
        self.states = {}
        # grid size
        for i in range(rows):
            for j in range (cols):
                self.states[(i, j)] = "OFF"

    def set_state(self, row: int, col: int, state: str) -> None:
        """
        Sets the states of each cell in grid (array since this is in the backend class).
        :param row: length of rows
        :param col: length of columns
        :param state: the new state of the cell
        :return None:
        """
        self.states[(row, col)] = state
        return

    def check_state(self, row: int, col: int) -> str:
        """
        The search algorithm will use this to determine the state of next cell/move and if the search is completed,
        blocked or another move is required.
        :param row: length of rows
        :param col: length of columns
        :return str: the state of the referenced cell
        """
        return self.states[(row, col)]