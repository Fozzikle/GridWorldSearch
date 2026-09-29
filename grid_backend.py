from node import Node


class GridBackEnd:
    def __init__(self, rows, cols):
        self.grid = {}

        # construct nodes
        for i in range(rows):
            for j in range(cols):
                self.grid[i, j] = Node(state="OFF", row=i, col=j)

                if j > 0:
                    self.grid[i, j].next_up = self.grid[i, j - 1]
                    self.grid[i, j - 1].next_down = self.grid[i, j]

                if i > 0:
                    self.grid[i, j].next_left = self.grid[i - 1, j]
                    self.grid[i - 1, j].next_right = self.grid[i, j]


    def set_state(self, row: int, col: int, state: str) -> None:
        """
        Sets the states of each cell in grid (array since this is in the backend class).
        :param row: length of rows
        :param col: length of columns
        :param state: the new state of the cell
        :return None:
        """
        self.grid[(row, col)].state = state
        return

    def check_state(self, row: int, col: int) -> str:
        """
        The search algorithm will use this to determine the state of next cell/move and if the search is completed,
        blocked or another move is required.
        :param row: length of rows
        :param col: length of columns
        :return str: the state of the referenced cell
        """
        return self.grid[(row, col)].state