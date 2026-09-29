class BreadthFirstSearch:
    def __init__(self, controller, start, end):
        self.controller = controller
        self.start = start
        self.end = end

    def visit(self, item):
        pass

    def bfs(self):
        queue = [self.start]
        while len(queue) > 0:
            item = queue.pop(0)

            if not (item.state == "CHECKED" or item.state == "WALL"):
                self.visit(item)
                self.controller.update_node( , "CHECKED")
                for