from grid_connect import GridController
from Backend.node_state import NodeState
from Backend.node import Node


def is_start_or_end(node: Node) -> bool:
    """
    Checks if the provide Node's state is the starting position or end goal of the grid.
    :param node: A node/cell of the grid
    :return: Returns true if node is start or end else false
    """
    return node.state == NodeState.START or node.state == NodeState.END


def is_checked_or_wall(node: Node) -> bool:
    """
    Checks if the provide Node's state is a wall in the grid or if the selected search algorithm has already checked
    this node.
    :param node: A node/cell of the grid
    :return: Returns true if the node is a wall or already checked
    """
    return node.state == NodeState.CHECKED or node.state == NodeState.WALL


def visit_neighbours(controller: GridController, node: Node, queue: list[Node], came_from: list[Node]) -> None:
    neighbours = [node.next_up, node.next_down, node.next_left, node.next_right]
    for n in neighbours:
        if n is None:
            continue

        if not (is_checked_or_wall(n) or n.state == NodeState.FRONTIER):
            row, col = n.position
            if not is_start_or_end(n):
                controller.update_node(row, col, NodeState.FRONTIER)
            came_from[n] = node
            queue.append(n)
    return


def get_path_from_camefrom(came_from, shortest_path, node):
    shortest_path.append(node)
    if node.state == NodeState.START:
        return shortest_path

    return get_path_from_camefrom(came_from, shortest_path, node=came_from[node])

def path(controller: GridController, shortest_path):
    shortest_path.reverse()
    for node in shortest_path:
        row, col = node.position
        if not (node.state == NodeState.START):
            controller.update_node(row, col, NodeState.SHORTEST)
    return
