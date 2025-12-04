
fd = open("./input.txt", "rt")
ids = fd.read().split(",")

# valid is true, invalid is false

def getDeviders(number) -> list[int]:
    deviders = []
    for n in range(1, number):
        if number % n == 0:
            deviders.append(n)
    return deviders

def splitString(input: str, parts: int) -> list[str]:
    word = []
    for i in range(0,len(input), parts):
        word.append(input[i:i + parts])

    return word

# valid is true, invalid is false
def checkNumber(n) -> bool:
    word = str(n)
    deviders = getDeviders(len(word))
    for dev in deviders:
        splittedWord = splitString(word, dev)
        partsAreEqual = True
        for i in range(1,len(splittedWord)):
            if not (splittedWord[0] == splittedWord[i]):
                partsAreEqual = False 
        
        if partsAreEqual:
            return False

    return True

countInvalid = 0
for e in ids:
    start = int(e.split("-")[0])
    end = int (e.split("-")[1])

    for number in range(start, end+1):
        if (not checkNumber(number)):
            countInvalid += number


print(countInvalid)