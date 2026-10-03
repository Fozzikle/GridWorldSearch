from grid_connect import GridController
from Backend.node import Node
from Backend.node_state import NodeState
from SearchAlgorithms.helper_functions import is_checked_or_wall, visit_neighbours, get_path_from_camefrom, path


class BreadthFirstSearch:
    def __init__(self, controller: GridController, start: Node, end: Node):
        self.controller: GridController = controller
        self.start: Node = start
        self.end: Node = end

    def bfs(self):
        queue: list[Node] = [self.start]
        came_from: list[Node] = {}
        shortest_path = []

        while len(queue) > 0:
            item = queue.pop(0)

            if item.position == self.end.position:
                shortest_path = get_path_from_camefrom(came_from, shortest_path, came_from[self.end])
                path(self.controller, shortest_path)
                return

            if not is_checked_or_wall(item):
                # 'visiting' the node
                row, col = item.position
                if not (item.state == NodeState.START):
                    self.controller.update_node(row, col, NodeState.CHECKED)

                visit_neighbours(self.controller, item, queue, came_from)
        return