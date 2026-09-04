class GridView:
    def __init__(self, canvas, rows, cols):
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

                item_id = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                self.id_map[(i, j)] = item_id