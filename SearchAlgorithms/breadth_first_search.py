class BreadthFirstSearch:
    def __init__(self, controller, start, end):
        self.controller = controller
        self.start = start
        self.end = end

    def bfs(self):
        queue = [self.start]
        came_from = {}
        shortest_path = []

        while len(queue) > 0:
            item = queue.pop(0)

            if item.position == self.end.position:
                shortest_path = self.find_shortest_path(came_from[self.end], shortest_path)
                print(shortest_path)
                return

            if not (item.state == "CHECKED" or item.state == "WALL"):
                # 'visiting' the node
                row, col = item.position
                if not (item.state == "START"):
                    self.controller.update_node(row, col, "CHECKED")

                # visit neighbours of item
                neighbours = [item.next_up, item.next_down, item.next_left, item.next_right]
                for n in neighbours:
                    if n is None:
                        continue

                    if not (n.state == "CHECKED" or n.state == "WALL" or n.state == "FRONTIER"):
                        row, col = n.position
                        if not (n.state == "START" or n.state == "END"):
                            self.controller.update_node(row, col, "FRONTIER")
                        came_from[n] = item
                        queue.append(n)
        return

    def find_shortest_path(self, came_from, node, shortest_path):
        node = came_from[node]
        if came_from.state == "START":
            return shortest_path
        return self.find_shortest_path(came_from, node=came_from[node], shortest_path.append(node))