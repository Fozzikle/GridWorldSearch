import heapq as hp
from grid_connect import GridController
from node import Node
from node_state import NodeState
from SearchAlgorithms.helper_functions import get_path_from_camefrom, path, is_checked_or_wall, is_start_or_end

class Dijkstra:
    def __init__(self, controller: GridController, start: Node, end: Node):
        self.controller: GridController = controller
        self.start: Node = start
        self.end: Node = end

    def dijkstra(self):
        # create heapq and distance array
        distance = {}
        queue = []
        came_from = {self.start: self.start}
        shortest_path = []

        # set distance of start to 0 and all other elements to infinity
        distance.update({self.start: (0, came_from[self.start])})
        hp.heappush(queue, (distance[self.start][0], self.start))




        # loop through heapq until empty and:
        while len(queue) > 0:
            # todo: pop based on shortest distance
            item: Node = hp.heappop(queue)[1]

            # record the distance from start to this node
            if item.state != NodeState.START and len(distance) > 0:
                item_distance = item.weight + distance[came_from[item]][0]

                # if this distance is less than the current shortest distance to this node update distance otherwise discard
                if item_distance < distance[item][0]:
                    distance[item] = (item_distance, came_from[item])

            # add neighbours to queue
            # todo: within visit neighbours set their distances to infinity
            neighbours = [item.next_up, item.next_down, item.next_left, item.next_right]
            for n in neighbours:
                if n is None:
                    continue

                # TODO: Update this part of neighbour
                if not (is_checked_or_wall(n) or n.state == NodeState.FRONTIER):
                    row, col = n.position
                    if not is_start_or_end(n):
                        self.controller.update_node(row, col, NodeState.FRONTIER)
                    came_from[n] = item
                    distance_from_neighbour: int = distance[came_from[item]][0] + distance[came_from[item]].weight
                    distance.update({item: (distance_from_neighbour, came_from[item])})
                    hp.heappush(queue, (distance[n][0], n))

            # repeat the search until it records the distance from the end node.
            # return the node trace of the shortest distance to end from start
            if item.state == NodeState.END:
                break





        # reconstruct shortest path
        # TODO
        found_path = get_path_from_camefrom(came_from, shortest_path, came_from[self.end])
        path(self.controller, found_path)
