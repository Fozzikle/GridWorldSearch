import unittest
from SearchAlgorithms import helper_functions
from node import Node
from node_state import NodeState

class TestHelperFunctions(unittest.TestCase):
    # Creating nodes of all the different states refer to NodeState class
    nodeStart = Node(state=NodeState.START, row=None, col=None)
    nodeEnd = Node(state=NodeState.END, row=None, col=None)
    nodeWALL = Node(state=NodeState.WALL, row=None, col=None)
    nodeFrontier = Node(state=NodeState.FRONTIER, row=None, col=None)
    nodeChecked = Node(state=NodeState.CHECKED, row=None, col=None)
    nodeSHORTEST = Node(state=NodeState.SHORTEST, row=None, col=None)
    nodeOFF = Node(state=NodeState.OFF, row=None, col=None)

    def test_is_start_or_end(self):
        # todo: add tests for wrong argument being passed

        # Testing correct returns based on different states
        self.assertEqual(helper_functions.is_start_or_end(self.nodeStart), True)
        self.assertEqual(helper_functions.is_start_or_end(self.nodeEnd), True)
        self.assertEqual(helper_functions.is_start_or_end(self.nodeWALL), False)
        self.assertEqual(helper_functions.is_start_or_end(self.nodeFrontier), False)
        self.assertEqual(helper_functions.is_start_or_end(self.nodeChecked), False)
        self.assertEqual(helper_functions.is_start_or_end(self.nodeSHORTEST), False)
        self.assertEqual(helper_functions.is_start_or_end(self.nodeOFF), False)

    def test_is_checked_or_wall(self):
        # todo: add tests for wrong argument being passed

        # Testing correct returns based on different states
        self.assertEqual(helper_functions.is_checked_or_wall(self.nodeStart), False)
        self.assertEqual(helper_functions.is_checked_or_wall(self.nodeEnd), False)
        self.assertEqual(helper_functions.is_checked_or_wall(self.nodeWALL), True)
        self.assertEqual(helper_functions.is_checked_or_wall(self.nodeFrontier), False)
        self.assertEqual(helper_functions.is_checked_or_wall(self.nodeChecked), True)
        self.assertEqual(helper_functions.is_checked_or_wall(self.nodeSHORTEST), False)
        self.assertEqual(helper_functions.is_checked_or_wall(self.nodeOFF), False)