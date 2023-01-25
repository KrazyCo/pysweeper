from tkinter import *
import random
import time

class Node:
    def __init__(self, x, y, value):
        self.x = x 
        self.y = y
        self.value = value
        self.isBomb = False
        self.isFlagged = False
        self.isRevealed = False
        self.button = Button(gridFrame, text=" ", width=2, height=1, command=self.reveal, bg="#808080").grid(row=self.y, column=self.x)

    def reveal(self):
        if self.isBomb:
            # print("You lose!")
            self.button = Button(gridFrame, text=" ", width=2, height=1, bg="#f00").grid(row=self.y, column=self.x)
            # time.sleep(3)
            # revealAll()
        else:
            self.isRevealed = True
            match self.value:
                case 0:
                    self.button = Button(gridFrame, text=" ", width=2, height=1).grid(row=self.y, column=self.x)
                    for x2 in range(self.x - 1, self.x + 2):
                        for y2 in range(self.y - 1, self.y + 2):
                            if not (x2 == self.x and y2 == self.y):
                                if x2 >= 0 and x2 < xWidth2 and y2 >= 0 and y2 < yHeight2:
                                    if not grid[x2][y2].isRevealed:
                                        grid[x2][y2].reveal()
                case 1:
                    self.button = Button(gridFrame, text="1", width=2, height=1, fg="#0000f2").grid(row=self.y, column=self.x)
                case 2:
                    self.button = Button(gridFrame, text="2", width=2, height=1, fg="#067d00").grid(row=self.y, column=self.x)
                case 3:
                    self.button = Button(gridFrame, text="3", width=2, height=1, fg="#fc0507").grid(row=self.y, column=self.x)
                case 4:
                    self.button = Button(gridFrame, text="4", width=2, height=1, fg="#010176").grid(row=self.y, column=self.x)
                case 5:
                    self.button = Button(gridFrame, text="5", width=2, height=1, fg="#84060d").grid(row=self.y, column=self.x)
                case 6:
                    self.button = Button(gridFrame, text="6", width=2, height=1, fg="#027d8b").grid(row=self.y, column=self.x)
                case 7:
                    self.button = Button(gridFrame, text="7", width=2, height=1, fg="#020202").grid(row=self.y, column=self.x)
                case 8:
                    self.button = Button(gridFrame, text="8", width=2, height=1, fg="#818181").grid(row=self.y, column=self.x)

def revealAll():
    for x in range(xWidth2):
        for y in range(yHeight2):
            if not grid[x][y].isRevealed:
                grid[x][y].reveal()

root = Tk()
root.geometry("500x600")

global gridFrame
gridFrame = Frame(root)
gridFrame.pack()

def setup(xWidth=20, yHeight=20, mineNum=40):
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
            # print("Mine placed at " + str(x) + ", " + str(y))

    for x in range(xWidth):
        for y in range(yHeight):
            for x2 in range(x - 1, x + 2):
                for y2 in range(y - 1, y + 2):
                    if not (x2 == x and y2 == y):
                        if x2 >= 0 and x2 < xWidth and y2 >= 0 and y2 < yHeight:
                            if grid[x2][y2].isBomb:
                                grid[x][y].value += 1

# for x in range(xWidth):
#     for y in range(yHeight):
#         grid[x][y].reveal()

Button(root, text="Reset", command=setup).pack()
Button(root, text="Reveal", command=revealAll).pack()

setup()

root.title("PySweeper")
root.mainloop()