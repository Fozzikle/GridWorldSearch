class Node:
    def __init__(self, state: str, row: int, col: int):
        self.state = state
        self.position = (row, col) # may not need
        self.next_up = None
        self.next_down = None
        self.next_left = None
        self.next_right = None