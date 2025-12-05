"""
    idea: 
        1. search first biggest number with index between 0 and len-12 (because we want the first digit as high as possible and 12 digits)
        2. search for the biggest number with index between previous index  and len-11
        ... repeat until 12 digits
        3. concatenate all numbers and add them up
"""

def searchBiggestNumber(bank: str, startIndex: int, stopIndex: int) -> tuple:
   
    biggestNumber = 0
    biggestNumberIndex = 0

    for index in range(startIndex,stopIndex):
        if int(bank[index]) > biggestNumber:
            biggestNumber = int(bank[index])
            biggestNumberIndex = index

    return (biggestNumberIndex, str(biggestNumber))


fd = open("./input.txt", "rt")

lines = fd.readlines()
solution = 0

for batteryBank in lines:
    batteryBank = batteryBank.strip()
    previousIndex = 0
    biggestNumber = ""
    for i in range (11,-1,-1):
        previousIndex, number = searchBiggestNumber(batteryBank, previousIndex, len(batteryBank)-i)
        previousIndex += 1
        biggestNumber += number
    solution += int(biggestNumber)

print(solution)