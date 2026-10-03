from node_state import NodeState

def is_start_or_end(item):
    return item.state == NodeState.START or item.state == NodeState.END

def is_checked_or_wall(item):
    return item.state == NodeState.CHECKED or item.state == NodeState.WALL