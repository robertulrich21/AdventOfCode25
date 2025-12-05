"""
Idea:
    1. create 2d Array --> count rows, cols
    2. go trough all entrys and check surrounding, if greater 4 remove paperS
"""

def checkSurronding(grid, x,y):
    paperRollCounter = 0
    
    #check north
    if y > 0:
        if grid[y-1][x] == "@":
            paperRollCounter +=1
    # check south
    if y < len(grid)-1:
        if grid[y+1][x] == "@":
            paperRollCounter +=1

    # check west
    if x > 0:
        if grid[y][x-1] == "@":
            paperRollCounter +=1
    # check east
    if x < len(grid[y])-1:
        if grid[y][x+1] == "@":
            paperRollCounter +=1

    # check NW:
    if y > 0 and x > 0:
        if grid[y-1][x-1] == "@":
            paperRollCounter +=1
    #check NE:
    if y > 0 and x < len(grid[y])-1:
        if grid[y-1][x+1] == "@":
            paperRollCounter +=1
    
    #check SW:
    if y < len(grid)-1 and x > 0:
        if grid[y+1][x-1] == "@":
            paperRollCounter +=1
    
    # check SE:
    if y < len(grid)-1 and x < len(grid[y])-1:
        if grid[y+1][x+1] == "@":
            paperRollCounter +=1

    return paperRollCounter


fd = open("./input.txt", "rt")
lines = fd.readlines()
lines = [a.strip() for a in lines]

removePaperRollCounter = 0

for i in range(0, len(lines)):
    for j in range (0, len(lines[i])):
        if lines[i][j] == "@":
            if checkSurronding(lines, j,i) < 4:
                removePaperRollCounter +=1

print(removePaperRollCounter)