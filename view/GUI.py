import tkinter as tk
from math import floor
from tkinter import W, RIGHT, BOTTOM, TOP, LEFT

from model.MatrixUpdater import MatrixUpdater
from model.Matrix import Matrix
from model.Cell import Cell


# Some important variables
mUpdater = MatrixUpdater()
matrix = mUpdater.getStartState()
matrixArray = matrix.getL2()
matrixCol = matrix.getCols()
matrixRow = matrix.getRows()
numGames = mUpdater.getIterations()
mTotalWeight = mUpdater.getTotalWeight()
root = tk.Tk()
height = 1500
width = 1500
heightMap = 500
widthMap = 500

canvas = tk.Canvas(root, height=height, width=width)

# Creates a slider where max value is number of iterations in a game
slider = tk.Scale(root, from_=0, to=numGames, length=500, orient=tk.HORIZONTAL, label="Number of Games")
slider.place(relx=0, rely=.9)

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
        x1, y1 = x0 + rect_width - 1, y0 + rect_height - 1
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

# text area

instructionsLabel = tk.Label(root, text="Pick your game and parameters!")
instructionsLabel.place(relx=.6, rely=0)

errorLabel = tk.Label(root, text="Error rate (default 0)")
errorTextArea = tk.Entry(root, width=50)
errorLabel.place(relx=.6, rely=.1)
errorTextArea.place(relx=.6, rely=.15)

deltaLabel = tk.Label(root, text="Discount rate/delta factor (default 0)")
deltaTextArea = tk.Entry(root)
deltaLabel.place(relx=.6, rely=.2)
deltaTextArea.place(relx=.6, rely=.25)

gamesPlayedLabel = tk.Label(root, text="Games played (default 10)")
gamesPlayedTextArea = tk.Entry(root)
gamesPlayedLabel.place(relx=.6, rely=.3)
gamesPlayedTextArea.place(relx=.6, rely=.35)

payoffInstructionLabel = tk.Label(root, text="Input payoffs. For non symmetric games, please enter payoffs of player "
                                             "\n 1 and player 2, separated by a comma (no spaces) ")
payoffInstructionLabel.place(relx=.6, rely=.4)

matrixFrame = tk.Frame(root, height=height / 6, width=height / 4.5, bg="light blue")
matrixFrame.place(relx=.6, rely=.45)

importButton = tk.Button(root, text="Import CSV", height=3, width=11)
importButton.place(relx=.7, rely=.85)

# add text boxes to array
labelArray = []

l1 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l1)

l2 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l2)

l3 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l3)

l4 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l4)

l5 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l5)

l6 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l6)

l7 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l7)

l8 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l8)

l9 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l9)

l10 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l10)

l11 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l11)

l12 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l12)

l13 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l13)

l14 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l14)

l15 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l15)

l16 = tk.Text(matrixFrame, height=2, width=10)
labelArray.append(l16)


# submit button to gather user inputted payoffs
def submitCommand():
    i = 0
    while i < 16:
        gridDict = {
            i: labelArray[i].get(1.0, "end")
        }
        i += 1
        return gridDict



submitButton = tk.Button(matrixFrame, height=1, width=10, text="Submit", activebackground="blue",
                         command=submitCommand)
submitButton.place(relx=.3, rely=.9)

# places text entries in grid format
l1.place(relx=0, rely=.1)
l2.place(relx=.25, rely=.1)
l3.place(relx=.5, rely=.1)
l4.place(relx=.75, rely=.1)

l5.place(relx=0, rely=.3)
l6.place(relx=.25, rely=.3)
l7.place(relx=.5, rely=.3)
l8.place(relx=.75, rely=.3)

l9.place(relx=0, rely=.5)
l10.place(relx=.25, rely=.5)
l11.place(relx=.5, rely=.5)
l12.place(relx=.75, rely=.5)

l13.place(relx=0, rely=.7)
l14.place(relx=.25, rely=.7)
l15.place(relx=.5, rely=.7)
l16.place(relx=.75, rely=.7)

canvas.place(relx=0, rely=0)
root.title("Roth-Erev Reinforcement")
root.mainloop()

