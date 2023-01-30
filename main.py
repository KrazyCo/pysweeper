from tkinter import *
import random

global xWidthIn, yHeightIn, mineNumIn

# Change these values to change the size of the grid and the number of mines, when changing the size of the grid, make sure to change the size of the window 
xWidthIn = 20 # Can't do super large sizes due to recursion limit
yHeightIn = 20 # Reccomend 20x20 at 40 mines, 500x600 window size
mineNumIn = 4
windiowSize = "500x600"

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.isBomb = False
        self.isFlagged = False
        self.isRevealed = False
        self.button = Button(gridFrame, text=" ", width=2, height=1, bg="#808080")
        self.button.grid(row=self.y, column=self.x)
        self.button.bind("<Button-1>", self.reveal)
        self.button.bind("<Button-3>", self.flag)

    def reveal(self, event):
        normal = False if event == "All" or event == "Won" else True
        if self.isBomb:
            self.button = Button(gridFrame, text="X", width=2, height=1, bg=("#f00" if normal else (("#8b0000" if not event == "Won" else "#008100") if not self.isFlagged else "#0f0"))).grid(row=self.y, column=self.x)
            self.isRevealed = True
            print(f"{event = }")
            if normal: revealAll()
        else:
            self.isRevealed = True
            match self.value:
                case 0:
                    self.button = Button(gridFrame, text=" ", width=2, height=1, bg=("#fff" if normal else "#aaaaaa")).grid(row=self.y, column=self.x)
                    for x2 in range(self.x - 1, self.x + 2):
                        for y2 in range(self.y - 1, self.y + 2):
                            if not (x2 == self.x and y2 == self.y):
                                if x2 >= 0 and x2 < xWidth2 and y2 >= 0 and y2 < yHeight2:
                                    if not grid[x2][y2].isRevealed:
                                        grid[x2][y2].reveal("Recursion" if normal else "All")
                case 1:
                    self.button = Button(gridFrame, text="1", width=2, height=1, fg="#0000f2", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
                case 2:
                    self.button = Button(gridFrame, text="2", width=2, height=1, fg="#067d00", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
                case 3:
                    self.button = Button(gridFrame, text="3", width=2, height=1, fg="#fc0507", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
                case 4:
                    self.button = Button(gridFrame, text="4", width=2, height=1, fg="#010176", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
                case 5:
                    self.button = Button(gridFrame, text="5", width=2, height=1, fg="#84060d", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
                case 6:
                    self.button = Button(gridFrame, text="6", width=2, height=1, fg="#027d8b", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
                case 7:
                    self.button = Button(gridFrame, text="7", width=2, height=1, fg="#020202", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
                case 8:
                    self.button = Button(gridFrame, text="8", width=2, height=1, fg="#818181", bg=("#fff" if normal else ("#aaaaaa" if not self.isFlagged else "#da8ee8"))).grid(row=self.y, column=self.x)
            if checkWin():
                revealAll("Won")
                print(f"{revealAll() = }")

    def flag(self, event):
        if self.isFlagged:
            self.isFlagged = False
            self.button = Button(gridFrame, text=" ", width=2, height=1, bg="#808080")
            self.button.grid(row=self.y, column=self.x)
            self.button.bind("<Button-1>", self.reveal)
            self.button.bind("<Button-3>", self.flag)
        else:
            self.isFlagged = True
            self.button = Button(gridFrame, text="F", width=2, height=1, bg="#000", fg="#f00")
            self.button.grid(row=self.y, column=self.x)
            self.button.bind("<Button-1>", self.reveal)
            self.button.bind("<Button-3>", self.flag)
        if checkWin():
            revealAll("Won")

def checkWin():
    for x in range(xWidth2):
        for y in range(yHeight2):
            if not grid[x][y].isBomb and not grid[x][y].isRevealed:
                return False
    return True

def revealAll(event="All"):
    for x in range(xWidth2):
        for y in range(yHeight2):
            if not grid[x][y].isRevealed:
                grid[x][y].reveal(event)

root = Tk()
root.geometry(windiowSize)

global gridFrame
gridFrame = Frame(root)
gridFrame.pack()

def setup(xWidth=xWidthIn, yHeight=yHeightIn, mineNum=mineNumIn):
    global grid, xWidth2, yHeight2
    xWidth2, yHeight2 = xWidth, yHeight
    grid = [[0 for y in range(yHeight)] for x in range(xWidth)]
    for x in range(xWidth):
        for y in range(yHeight):
            grid[x][y] = Node(x, y, 0)

    while mineNum > 0:
        x = random.randint(0, xWidth - 1)
        y = random.randint(0, yHeight - 1)
        if not grid[x][y].isBomb:
            grid[x][y].isBomb = True
            mineNum -= 1

    for x in range(xWidth):
        for y in range(yHeight):
            for x2 in range(x - 1, x + 2):
                for y2 in range(y - 1, y + 2):
                    if not (x2 == x and y2 == y):
                        if x2 >= 0 and x2 < xWidth and y2 >= 0 and y2 < yHeight:
                            if grid[x2][y2].isBomb:
                                grid[x][y].value += 1

Button(root, text="Reset", command=setup).pack()
Button(root, text="Reveal", command=revealAll).pack()

setup()

root.title("PySweeper")
root.mainloop()