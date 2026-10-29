import unittest
import numpy as np
import tkinter as tk
from grid_backend import GridBackEnd
from grid_connect import GridController
from grid_frontend import GridFrontEnd


class TestBreadthFirstSearch(unittest.TestCase):
    rng = np.random.default_rng()
    number: int = int(rng.integers(1, 1000, 1))
    row: int = number
    col: int = number

    # has no effect on testing just needed for args
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=600)
    cell_size: int = 20
    model_frontend = GridFrontEnd(canvas, row, col, cell_size)

    model_backend = GridBackEnd(row, col)
    controller = GridController(model_frontend, model_backend)

    start = int(rng.integers(1, number, 1))
    end = int(rng.integers(1, number, 1))

    def test_bfs(self):
        pass