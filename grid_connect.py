class GridController:
    def __init__(self, frontend,  backend):
        self.frontend = frontend
        self.backend = backend

    # Defining attribute map for state
    _colour_map = {
        "OFF": "blue",
        "WALL": "black",
        "START": "green",
        "END": "red"
    }
    def get_colour_map(self) -> dict:
        return self._colour_map

    def update_cell(self, row: int, col: int, new_state: str) -> None:
        """
        This function updates the frontend and backend grids such that each cell's states are reflective in both.
        Takes in the positional coordinates of row and column and applies the new state to the backend cell and updates
        the rectangle's colour of the frontend based on the colour mapping defined in the file grid_connect.py
        :param row:
        :param col:
        :param new_state:
        :return:
        """
        self.backend.states[(row, col)] = new_state
        updated_colour: str = self._colour_map[new_state]
        self.frontend.set_state(row, col, updated_colour)
        return