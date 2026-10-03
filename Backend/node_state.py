from enum import Enum


class NodeState(Enum):
    OFF = "OFF"
    WALL = "WALL"
    START = "START"
    END = "END"
    FRONTIER = "FRONTIER"
    CHECKED = "CHECKED"
    SHORTEST = "SHORTEST"

