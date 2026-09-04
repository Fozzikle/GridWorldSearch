class Grid:
    def __init__(self, rows, cols):
        self.states = {}
        # grid size
        for i in range(rows):
            for j in range (cols):
                self.states[(i, j)] = "OFF"