import tkinter as tk
from grid_backend import GridBackEnd
from grid_frontend import GridFrontEnd

# making the window
root = tk.Tk()
root.title("Grid World Search")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()


# Creating the grids
row: int = 20
col: int = 20
model_frontend = GridFrontEnd(canvas, row, col)
model_backend = GridBackEnd(row, col)



root.mainloop()