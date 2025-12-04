
fd = open("./input.txt", "r")
file = fd.readlines()
currentNumber = 50
countZero = 0

for l in file:
    direction = l.strip()[0:1]
    steps = int(l.strip()[1:])

    for tick in range(0,steps):

        if direction == "L":
            currentNumber = (currentNumber - 1) % 100
        else:
            currentNumber = (currentNumber + 1) % 100

        if currentNumber == 0:
            countZero +=1

print (countZero)