import tkinter as tk
from grid_backend import GridBackEnd
from grid_connect import GridController
from grid_frontend import GridFrontEnd


def cell_press(event) -> None:
    global press_count
    state = "OFF"

    print('Got object click', event.x, event.y)
    row: int = event.x // cell_size
    col: int = event.y // cell_size
    print("Selected rectangle", row, col)

    if press_count == 0:
        state: str = "START"
        press_count += 1

    elif press_count == 1:
        state: str = "END"
        press_count += 1

    elif press_count > 1 and GridBackEnd.check_state(model_backend, row, col) == "OFF":
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

# Selections
controller = GridController(model_frontend, model_backend)
press_count = 0

# Reset button
# TODO: figure out why the reset action is breaking frontend grid set (most likely the command is being ran at start)
reset = tk.Button(canvas, text="Reset Grid", width=40, height=5, command=controller.update_cell(row, col, "OFF"))
reset.place(x=100, y=500)

# Adding button actions to the cells
canvas.bind("<Button-1>", cell_press)


# Add side bar
# TODO: as per outline documentation

root.mainloop()