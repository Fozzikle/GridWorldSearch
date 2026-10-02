from node_state import NodeState


class Node:
    def __init__(self, state: NodeState, row: int, col: int):
        self.state = state
        self.position = (row, col) # may not need
        self.next_up = None
        self.next_down = None
        self.next_left = None
        self.next_right = None