from grid_connect import GridController
from node import Node
from node_state import NodeState


class BreadthFirstSearch:
    def __init__(self, controller: GridController, start: Node, end: Node):
        self.controller: GridController = controller
        self.start: Node = start
        self.end: Node = end

    def bfs(self):
        queue: list[Node] = [self.start]
        came_from = {}
        shortest_path = []

        while len(queue) > 0:
            item = queue.pop(0)

            if item.position == self.end.position:
                shortest_path = self.find_shortest_path(came_from, shortest_path, came_from[self.end])
                shortest_path.reverse()
                for node in shortest_path:
                    row, col = node.position
                    if not (node.state == NodeState.START):
                        self.controller.update_node(row, col, NodeState.SHORTEST)
                return

            if not (item.state == NodeState.CHECKED or item.state == NodeState.WALL):
                # 'visiting' the node
                row, col = item.position
                if not (item.state == NodeState.START):
                    self.controller.update_node(row, col, NodeState.CHECKED)

                # visit neighbours of item
                neighbours = [item.next_up, item.next_down, item.next_left, item.next_right]
                for n in neighbours:
                    if n is None:
                        continue

                    if not (n.state == NodeState.CHECKED or n.state == NodeState.WALL or n.state == NodeState.FRONTIER):
                        row, col = n.position
                        if not (n.state == NodeState.START or n.state == NodeState.END):
                            self.controller.update_node(row, col, NodeState.FRONTIER)
                        came_from[n] = item
                        queue.append(n)
        return

    def find_shortest_path(self, came_from, shortest_path, node):
        shortest_path.append(node)
        if node.state == NodeState.START:
            return shortest_path

        return self.find_shortest_path(came_from, shortest_path, node=came_from[node])