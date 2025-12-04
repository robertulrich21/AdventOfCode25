
fd = open("./input.txt", "rt")
ids = fd.read().split(",")

# valid is true, invalid is false
def checkPattern(n) -> bool:
    word = str(n)
    if word[:int(len(word)/2)] == word[int(len(word)/2):]:
        return False
    
    return True


countInvalid = 0
for e in ids:
    start = int(e.split("-")[0])
    end = int (e.split("-")[1])

    for number in range(start, end+1):
        if (not checkPattern(number)):
            countInvalid += number


print(countInvalid)