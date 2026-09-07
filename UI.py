import tkinter as tk
from grid_backend import GridBackEnd
from grid_connect import GridController
from grid_frontend import GridFrontEnd

# TODO: prevent wall from overriding start or end.
def cell_press(event):
    global press_count

    print('Got object click', event.x, event.y)
    row = event.x // cell_size
    col = event.y // cell_size
    print("Selected rectangle", row, col)

    # TODO: fix
    # if model_backend.check_state(row, col) == "Start":
    #     state: str = "OFF"
    #     press_count = 0

    if press_count == 0:
        state: str = "START"
        press_count += 1

    elif press_count == 1:
        state: str = "END"
        press_count += 1

    else:
        state: str = "WALL"
        press_count += 1

    controller.update_cell(row, col, state)
    return

# making the window
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
controller = GridController(model_frontend, model_backend)
press_count = 0

# Adding button actions to the cells
canvas.bind("<Button-1>", cell_press)

root.mainloop()