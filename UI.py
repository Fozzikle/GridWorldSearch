import tkinter as tk
from Backend.grid_backend import GridBackEnd
from grid_connect import GridController
from grid_frontend import GridFrontEnd
from Backend.node_state import NodeState
from SearchAlgorithms.breadth_first_search import BreadthFirstSearch
from SearchAlgorithms.depth_first_search import DepthFirstSearch


def cell_press(event) -> None:
    """
    Calls to update the frontend cell states such they match
    :param event:
    :return:
    """
    global press_count
    global start
    global end

    # Location of user click
    print('Got object click', event.x, event.y)

    # Normalising user click to a cell reference
    row: int = event.x // cell_size
    col: int = event.y // cell_size
    print("Selected rectangle", row, col)
    state = model_backend.check_state(row, col)

    if press_count == 0:
        state: NodeState = NodeState.START
        press_count += 1
        start = (row, col)

    elif press_count == 1:
        state: NodeState = NodeState.END
        press_count += 1
        end = (row, col)

    elif press_count > 1 and GridBackEnd.check_state(model_backend, row, col) == NodeState.OFF:
        state: NodeState = NodeState.WALL
        press_count += 1

    controller.update_node(row, col, state)
    return


def reset_event() -> None:
    global press_count

    controller.reset_grid(row, col, NodeState.OFF)
    press_count = 0

def bfs() -> None:
    bfs_object = BreadthFirstSearch(controller, model_backend.get_node(start), model_backend.get_node(end))
    bfs_object.bfs()

def dfs() -> None:
    dfs_object = DepthFirstSearch(controller, model_backend.get_node(start), model_backend.get_node(end))
    dfs_object.dfs()


# making the window
# TODO: make the window adjustable with the objects scaling to match
root = tk.Tk()
root.title("Grid World Search")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Creating the grids
row: int = 20
col: int = 20
cell_size: int = 20
model_frontend = GridFrontEnd(canvas, row, col, cell_size)
model_backend = GridBackEnd(row, col)

# Selections
controller = GridController(model_frontend, model_backend)
press_count = 0
start = ()
end = ()

# Reset button
# TODO: Format and stylise the button appropriately
reset = tk.Button(canvas,
                  text="Reset Grid",
                  width=20,
                  height=1,
                  command=lambda: reset_event())
reset.place(x=100, y=500)

# Adding button actions to the cells
canvas.bind("<Button-1>", cell_press)

# Add side bar
# TODO: as per outline documentation

# temp start button
start_button = tk.Button(canvas,
                         text="Start",
                         width=20,
                         height=1,
                         command=lambda: dfs())
start_button.place(x=400, y=500)


root.mainloop()