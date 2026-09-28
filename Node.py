class Node:
    def __init__(self, state: str):
        self.data = state
        self.next_up = None
        self.next_down = None
        self.next_left = None
        self.next_right = None
        self.previous = None

# yhing