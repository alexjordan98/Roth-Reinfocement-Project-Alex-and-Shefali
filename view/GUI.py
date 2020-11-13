import tkinter as tk
from model.MatrixUpdater import MatrixUpdater

mUpdater = MatrixUpdater()
numGames = mUpdater.getIterations()
root = tk.Tk()
canvas = tk.Canvas(root, height=1500, width=1500)
slider = tk.Scale(root, from_=0, to=numGames, length=500, orient=tk.HORIZONTAL, label="Number of Games")
slider.place(relx=0, rely=.9)
canvas.pack()
root.mainloop()
