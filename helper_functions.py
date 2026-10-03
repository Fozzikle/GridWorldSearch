from node_state import NodeState
from node import Node


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
