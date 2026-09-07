class GridBackEnd:
    def __init__(self, rows, cols):
        self.states = {}
        # grid size
        for i in range(rows):
            for j in range (cols):
                self.states[(i, j)] = "OFF"

    def set_state(self, row: int, col: int, state: str) -> None:
        self.states[(row, col)] = state
        return

    def check_state(self, row: int, col: int) -> str:
        return self.states[(row, col)]