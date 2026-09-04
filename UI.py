import tkinter as tk
import grid_view

root = tk.Tk()
root.title("Grid World Search")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()


# Creating grid
grid_view.GridView(canvas, 20, 20)


root.mainloop()