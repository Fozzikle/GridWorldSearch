from grid_connect import GridController
from node import Node
from node_state import NodeState
from SearchAlgorithms.helper_functions import is_checked_or_wall, is_start_or_end, visit_neighbours, get_path_from_camefrom, path


# TODO: When testing it is doing a bit of 'over searching' (checks other neighbours around the end as part of path)
class DepthFirstSearch:
    def __init__(self, controller: GridController, start: Node, end: Node):
        self.controller: GridController = controller
        self.start: Node = start
        self.end: Node = end

    def dfs(self):
        stack: list[Node] = [self.start]
        came_from: list[Node] = {}
        shortest_path = []

        self.step(stack, came_from)

        # found path (starts from end)
        found_path = get_path_from_camefrom(came_from, shortest_path, came_from[self.end])
        # corrects orientation and applies the visualisation
        path(self.controller, found_path)
        return

    def step(self, stack, came_from):
        if len(stack) <= 0:
            return None

        # Take last element of the stack
        item = stack.pop(-1)

        if item.state == NodeState.END:
            return None

        # visit item
        if not is_checked_or_wall(item):
            row, col = item.position
            if not is_start_or_end(item):
                self.controller.update_node(row, col, NodeState.CHECKED)

        # Add neighbours to stack
        if not (item.state == NodeState.WALL or item.state == NodeState.END):
            visit_neighbours(self.controller, item, stack, came_from)

        return self.step(stack, came_from)