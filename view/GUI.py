import tkinter as tk
from tkinter import filedialog

from colour import Color

from model.MatrixUpdater import MatrixUpdater
from model.Matrix import Matrix
from model.Cell import Cell

# Some important variables
l1 = [1, 1, 1, 1, 1]
l2 = [1, 1, 1, 1, 1]
updaterList = []
m4 = Matrix("m0", 4, 4, 0.2, 0.1, [], l1, l2)
mUpdater = MatrixUpdater(10, updaterList)

# m4.makeMatrix()

# updaterList contains states
# mUpdater.itter(m4)

# mTotalWeight = mUpdater.getTotalWeight()
root = tk.Tk()
height = 1500
width = 1500
heightMap = 500
widthMap = 500


canvas = tk.Canvas(root, height=height, width=width)



#print("this is of size " + str(len(listOfColorMatrix)))
#print(listOfColorMatrix)

# graphically prints heat map to a colored grid


# text area

instructionsLabel = tk.Label(root, text="Pick your game and parameters!")
instructionsLabel.place(relx=.6, rely=0)

errorLabel = tk.Label(root, text="Error rate (default 0)")
errorTextArea = tk.Entry(root, width=5)
errorLabel.place(relx=.6, rely=.1)
errorTextArea.place(relx=.6, rely=.15)
def getError():
    error = errorTextArea.get()
    if error == "":
        return float(0)
    else:
        return float(error)


deltaLabel = tk.Label(root, text="Discount rate/delta factor (default 0)")
deltaTextArea = tk.Entry(root, width=5)
deltaLabel.place(relx=.6, rely=.2)
deltaTextArea.place(relx=.6, rely=.25)
def getDelta():
    delta = deltaTextArea.get()
    if delta == "":
        return float(0)
    else:
        return float(delta)


gamesPlayedLabel = tk.Label(root, text="Games played (default 10)")
gamesPlayedTextArea = tk.Entry(root, width=5)
gamesPlayedLabel.place(relx=.6, rely=.3)
gamesPlayedTextArea.place(relx=.6, rely=.35)
def getGamesPlayed():
    gp = gamesPlayedTextArea.get()
    print(gp)
    if gp == "":
        return int(10)
    else:
        print("this is number of games" + gp)
        return int(gp)



payoffInstructionLabel = tk.Label(root, text="Input weights. Input payoffs. Please enter payoffs of player "
                                             "\n 1 and player 2, separated by a comma (no spaces) ")
payoffInstructionLabel.place(relx=.6, rely=.4)

matrixFrame = tk.Frame(root, height=height / 4, width=height / 5, bg="light blue")
matrixFrame.place(relx=.6, rely=.45)

rowsLabel = tk.Label(root, text="Input number of rows:")
rowsText = tk.Entry(root, width=5)
rowsLabel.place(relx=.85, rely=.5)
rowsText.place(relx=.85, rely=.55)

def getUserRows():
    rows = rowsText.get()
    print(rows)
    if rows == "":
        return 0
    else:
        return int(rowsText.get())

colsLabel = tk.Label(root, text="Input number of columns:")
colsText = tk.Entry(root, width=5)
colsLabel.place(relx=.85, rely=.6)
colsText.place(relx=.85, rely=.65)

def getUserCols():
    cols = colsText.get()
    print(cols)
    if cols == "":
        return 0
    return int(colsText.get())


def fileOpen():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    return filename


importButton = tk.Button(matrixFrame, text="Import CSV", height=2, width=11,
                         command=lambda: fileOpen())
importButton.place(relx=.6, rely=.9)

# add text boxes to array
labelArray = []

l1 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l1)

l2 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l2)

l3 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l3)

l4 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l4)

l5 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l5)

l6 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l6)

l7 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l7)

l8 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l8)

l9 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l9)

l10 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l10)

l11 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l11)

l12 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l12)

l13 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l13)

l14 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l14)

l15 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l15)

l16 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l16)

l17 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l17)

l18 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l18)

l19 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l19)

l20 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l20)

l21 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l21)

l22 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l22)

l23 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l23)

l24 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l24)

l25 = tk.Text(matrixFrame, height=2, width=5)
labelArray.append(l25)




# places text entries in grid format
#l1.place(relx=.2, rely=.02)
l2.place(relx=.35, rely=.02)
l3.place(relx=.5, rely=.02)
l4.place(relx=.65, rely=.02)
l5.place(relx=.8, rely=.02)

l6.place(relx=.02, rely=.25)
l7.place(relx=.35, rely=.25)
l8.place(relx=.5, rely=.25)
l9.place(relx=.65, rely=.25)
l10.place(relx=.8, rely=.25)

l11.place(relx=.02, rely=.4)
l12.place(relx=.35, rely=.4)
l13.place(relx=.5, rely=.4)
l14.place(relx=.65, rely=.4)
l15.place(relx=.8, rely=.4)


l16.place(relx=.02, rely=.55)
l17.place(relx=.35, rely=.55)
l18.place(relx=.5, rely=.55)
l19.place(relx=.65, rely=.55)
l20.place(relx=.8, rely=.55)

l21.place(relx=.02, rely=.7)
l22.place(relx=.35, rely=.7)
l23.place(relx=.5, rely=.7)
l24.place(relx=.65, rely=.7)
l25.place(relx=.8, rely=.7)

slider = tk.Scale(root)
# delta = float(0)
# epsilon = float(0)
# row = 0
# row = 0
# p1weight = []
# p2weight = []
# global actualMatrix
# actualMatrix = ("M1", 0, 0, epsilon, delta, [[]], p1weight, p2weight)
# amUpdater = MatrixUpdater(10, [])



def getIterationsFromSlider(self):
    global slider
    global mUpdater

    curIteration = int(slider.get() - 1)
    # print(curIteration)
    #colorMatrix = makeListofColorMatrix(numGames)[curIteration]
    #colorMatrix =
    # print(cm[int(slider.get() - 1)])
    print("at least ne 10 but maybe 15" + str(mUpdater.getIterations()))
    cm = makeListofColorMatrix(mUpdater.getIterations())
    rowsColor, colsColor = len(cm[int(slider.get() - 1)]), len(cm[int(slider.get() - 1)][0])
    rect_width, rect_height = widthMap // rowsColor, heightMap // colsColor
    for y, row in enumerate(cm[int(slider.get() - 1)]):
        for x, color in enumerate(row):
            x0, y0 = x * rect_width, y * rect_height
            x1, y1 = x0 + rect_width - 1, y0 + rect_height - 1
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)


# submit button to gather user inputted payoffs
def submitPayoffs():
    global m4
    global mUpdater
    delta = getDelta()
    epsilon = getError()
    rows = getUserRows()
    cols = getUserCols()
    iterations = getGamesPlayed()
    print("gp" + str(getGamesPlayed()))
    m4.setDelta(delta)
    m4.setEpsilon(epsilon)
    mUpdater.setIterations(iterations)
    print("i hope this is 15 " + str(mUpdater.getIterations()))

    i = 1
    p2weightlist = []
    p1weightlist = []
    p1Payoff = []
    p2Payoff = []
    while i < 25:
        curText = labelArray[i].get("1.0", "end")
        if curText != '' and curText != '\n':
            if i == 1 or i == 2 or i == 3 or i == 4:
                curWeight = float(curText)
                p2weightlist.append(curWeight)
            elif i == 5 or i == 10 or i == 15 or i == 20:
                curWeight = float(curText)
                p1weightlist.append(curWeight)
            else :
                p1Payoff.append(float(curText[0]))
                p2Payoff.append(float(curText[2]))
        i += 1

    l2 = []
    x = 0
    y = 0
    while x < rows:
        z = 0
        l3 = []
        while z < cols:
            l3.append(Cell(p1Payoff[y], p2Payoff[y], 0, 0, 0))
            y += 1
            z += 1
        l2.append(l3)
        x += 1

    m4.setp1Weights(p1weightlist)
    m4.setp2Weights(p2weightlist)
    m4.setRows(rows)
    m4.setCols(cols)
    mUpdater.itter(m4)

    global slider


    # Creates a slider where max value is number of iterations in a game
    slider = tk.Scale(root, from_=1, to=mUpdater.getIterations(), length=500, orient=tk.HORIZONTAL,
                      label="Number of Games",
                      command=getIterationsFromSlider)
    slider.place(relx=0, rely=.9)



submitButton = tk.Button(root, height=1, width=10, text="Submit", activebackground="blue",
                         command=lambda: [submitPayoffs()])
submitButton.place(relx=.65, rely=.9)

numGames = mUpdater.getIterations()
mUpdater.itter(m4)
matrix = mUpdater.states[0]
matrixArray = matrix.getL2()
matrixCol = matrix.getCols()
matrixRow = matrix.getRows()

def probToHex(prob : float):
    lightBlue = Color("#CDD9EE")
    darkBlue = Color("#02235B")
    colors = list(lightBlue.range_to(darkBlue, 101))
    probIndex = int(round(prob, 2) * 100)
    print("this is prob" + str(probIndex))
    return colors[probIndex]

def makeColorMatrix(matrixCol : int, matrixRow : int, matrixArray : []):
    colorMatrix = []
    for i in range(matrixCol):
        colorMatrixv2 = []
        for j in range(matrixRow):
            curProb = matrixArray[i][j].getProb()
            colorMatrixv2.append(probToHex(curProb))
        colorMatrix.append(colorMatrixv2)

    return colorMatrix


# Creates heat map of cells based on weights
def makeListofColorMatrix(numGames : int):
    listOfColorMatrix = []
    #global mUpdater
    for k in range(numGames):
        kthMatrix = mUpdater.states[k]
        matrixArray = kthMatrix.getL2()
        matrixCol = kthMatrix.getCols()
        matrixRow = kthMatrix.getRows()
        listOfColorMatrix.append(makeColorMatrix(matrixCol, matrixRow, matrixArray))
    return listOfColorMatrix

def makeWithSliderMax():
    print(str(mUpdater.getIterations()))
    cm = makeListofColorMatrix(mUpdater.getIterations())
    print("length is " + str(len(cm)))



canvas.place(relx=0, rely=0)
root.title("Roth-Erev Reinforcement")
root.mainloop()
