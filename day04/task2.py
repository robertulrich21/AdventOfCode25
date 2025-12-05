
"""
    Idea:
        1. while at least one @ got removed repeat
        2. go through all rows, cols, find @
        3. remove @ from grid if its surrounded by less than 4 @, add 1 to counter, set bool to true
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
grid = []
for c in lines:
    row = []
    c = c.strip()
    for r in c:
        row.append(r)
    grid.append(row)

removePaperRollCounter = 0

atGotRemoved = True
while atGotRemoved:
    atGotRemoved = False
    for i in range(0, len(grid)):
        for j in range (0, len(grid[i])):
            if grid[i][j] == "@":
                if checkSurronding(grid, j,i) < 4:
                    grid[i][j] = "x"
                    atGotRemoved = True
                    removePaperRollCounter +=1

print(removePaperRollCounter)