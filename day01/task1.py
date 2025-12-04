
fd = open("./input.txt", "r")
file = fd.readlines()
currentNumber = 50
countZero = 0

for l in file:
    direction = l.strip()[0:1]
    steps = int(l.strip()[1:])

    if direction == "L":
        currentNumber = (currentNumber - steps) % 100
            
    elif direction == "R":
        currentNumber = (currentNumber + steps) % 100
    
    if currentNumber == 0:
        countZero += 1

print (countZero)