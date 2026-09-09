class GridController:
    def __init__(self, frontend,  backend):
        self.frontend = frontend
        self.backend = backend

    # Defining attribute map for state
    __colour_map = {
        "OFF": "blue",
        "WALL": "black",
        "START": "green",
        "END": "red"
    }
    def get_colour_map(self) -> dict:
        return self.__colour_map

    def update_cell(self, row: int, col: int, new_state: str) -> None:
        """
        This function updates the frontend and backend grids such that each cell's states are reflective in both.
        Takes in the positional coordinates of row and column and applies the new state to the backend cell and updates
        the rectangle's colour of the frontend based on the colour mapping defined in the file grid_connect.py
        :param row: length of rows
        :param col: length of columns
        :param new_state: the new state of the cell (refer to __colour_map)
        :return None:
        """
        self.backend.states[(row, col)] = new_state
        updated_colour: str = self.__colour_map[new_state]
        print(updated_colour)
        self.frontend.set_state(row, col, updated_colour)
        return

    def reset_grid(self, row: int, col: int, state) -> None:
        """
        This function resets the state of all cells to a parsed state.
        :param row: length of rows
        :param col: length of columns
        :param state: the new state of the cell (refer to __colour_map)
        :return:
        """
        for i in range(row):
            for j in range(col):
                self.backend.states[i, j] = state
                update_colour: str = self.__colour_map[state]
                self.frontend.set_state(i, j, update_colour)
                return