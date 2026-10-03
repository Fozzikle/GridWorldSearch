import unittest
from grid_backend import GridBackEnd
from node import Node

class TestBackend(unittest.TestCase):
    rows = 20
    cols = 20
    backend = GridBackEnd(rows, cols)

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



if "__name__" == "__main__":
    unittest.main()