import unittest
import numpy as np
from grid_backend import GridBackEnd
from node import Node
from node_state import NodeState

class TestBackend(unittest.TestCase):
    rows = 20
    cols = 20
    backend = GridBackEnd(rows, cols)
    states = [NodeState.OFF, NodeState.START, NodeState.END, NodeState.CHECKED, NodeState.FRONTIER, NodeState.WALL,
              NodeState.SHORTEST]

    # First run Tests
    def test_backend_state(self):
        self.assertIsInstance(self.backend, GridBackEnd)

    def test_grid_size(self):
        self.assertEqual(len(self.backend.grid), 400)

    def test_node_state(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.assertIsInstance(self.backend.grid[i, j], Node)

    # Functions tests
    def test_set_state(self):
        rng = np.random.default_rng(1)
        for state in self.states:
            for i in range(100):
                row = rng.integers(0, self.rows, 1).item()
                col = rng.integers(0, self.cols, 1).item()
                self.backend.set_state(row, col, state=state)
                self.assertEqual(self.backend.grid[row, col].state, state)

    def test_check_state(self):
        rng = np.random.default_rng(1)
        for state in self.states:
            for i in range(100):
                row = rng.integers(0, self.rows, 1).item()
                col = rng.integers(0, self.cols, 1).item()
                self.backend.grid[row, col].state = state
                self.assertEqual(self.backend.check_state(row, col), state)

    def test_get_node(self):
        rng = np.random.default_rng(1)
        for i in range(100):
            row = rng.integers(0, self.rows, 1).item()
            col = rng.integers(0, self.cols, 1).item()
            self.assertIsInstance(self.backend.get_node((row, col)), Node)
            self.assertEqual(self.backend.get_node((row, col)), self.backend.grid[row, col])




if "__name__" == "__main__":
    unittest.main()