from grid_connect import GridController
from node import Node
from node_state import NodeState
import heapq as hp

class Dijkstra:
    def __init__(self, controller: GridController, start: Node, end: Node):
        self.controller: GridController = controller
        self.start: Node = start
        self.end: Node = end

    def dijkstra(self):
        # create heapq and distance array
        distance = {}
        queue = [self.start]
        camefrom = {self.start: self.start}

        # set distance of start to 0 and all other elements to infinity
        distance.update({self.start: (0, camefrom[self.start])})


        # loop through heapq until empty and:
        while len(queue) > 0:
            item: Node = hp.heappop(queue)

            # record the distance from start to this node
            if len(distance) > 0:
                item_distance = item.weight + distance[camefrom[[item]]]
            else:
                item_distance = 1

            # if this distance is less than the current shortest distance to this node update distance otherwise discard
            if item_distance < distance[item]:
                distance[item] = item_distance

            # repeat the search until it records the distance from the end node.
            # return the node trace of the shortest distance to end from start
            if item.state == NodeState.END:
                pass