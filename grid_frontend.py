class GridFrontEnd:
    def __init__(self, canvas, rows: int, cols: int):
        self.canvas = canvas
        self.id_map = {}

        # Creating grid of rectangles (fill colour is temp for now)
        cell_size = 20
        for i in range(rows):
            for j in range(cols):
                x1: int = i * cell_size
                y1: int = j * cell_size
                x2: int = i * cell_size + cell_size
                y2: int = j * cell_size + cell_size

                cell_id = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                self.id_map[(i, j)] = cell_id

    def set_state(self, row: int, col: int, state: str) -> None:
        try:
            cell_id = self.id_map[(row, col)]
            self.canvas.itemconfig(cell_id, fill=state)
        except KeyError:
            print("Failed to set state!")
            print("set_state(row, col, state)")
            exit(1)