import tkinter as tk
from math import floor

from model.MatrixUpdater import MatrixUpdater
from model.Matrix import Matrix
from model.Cell import Cell

root = tk.Tk()
height = 1500
width = 1500
heightMap = 500
widthMap = 500
canvas = tk.Canvas(root, height=height, width=width)

# Creates an instance of MatrixUpdater to extract number of games, which will be max value of slider
mUpdater = MatrixUpdater()
matrix = mUpdater.getStartState()
matrixArray = matrix.getL2()
matrixCol = matrix.getCols()
matrixRow = matrix.getRows()
numGames = mUpdater.getIterations()
slider = tk.Scale(root, from_=0, to=numGames, length=500, orient=tk.HORIZONTAL, label="Number of Games")
slider.place(relx=0, rely=.9)
mTotalWeight = mUpdater.getTotalWeight()

# replace this with mTotalWeight once fully written
fakeTotalWeight = 10

# Creates heat map of cells based on weights
colorMatrix = [[0 for x in range(matrixCol)] for x in range(matrixRow)]
for i in range(matrixCol):
    for j in range(matrixRow):
        curWeight = matrixArray[i][j].getWeight()
        # color for lowest weight proportional to total weight, bottom 20 percent
        if 0 <= curWeight < floor(fakeTotalWeight * .2):
            colorMatrix[i][j] = "ghost white"
        # 20-40 percent
        elif floor(fakeTotalWeight * .2) <= curWeight < floor(fakeTotalWeight * .4):
            colorMatrix[i][j] = "SkyBlue1"
        # 40-60 percent
        elif floor(fakeTotalWeight * .4) <= curWeight < floor(fakeTotalWeight * .6):
            colorMatrix[i][j] = "SkyBlue2"
        # 60-80 percent
        elif floor(fakeTotalWeight * .6) <= curWeight < floor(fakeTotalWeight * .8):
            colorMatrix[i][j] = "SkyBlue3"
        # 80-100 percent
        elif floor(fakeTotalWeight * .8) <= curWeight <= fakeTotalWeight:
            colorMatrix[i][j] = "SkyBlue4"

# graphically prints heat map to a colored grid
rowsColor, colsColor = len(colorMatrix), len(colorMatrix[0])
rect_width, rect_height = widthMap // rowsColor, heightMap // colsColor
for y, row in enumerate(colorMatrix):
    for x, color in enumerate(row):
        x0, y0 = x * rect_width, y * rect_height
        x1, y1 = x0 + rect_width-1, y0 + rect_height-1
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

canvas.pack()
root.mainloop()
