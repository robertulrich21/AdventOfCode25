"""
Idea: 
    1. search for the biggest number between index 0 and len(batteryBank) - 1 (exclude the last number)
        --> if there are multiple biggest numbers take the first one
    2. search for the biggest number between index of the first number and the last
    3. combine the numbers and add them to a variable

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
    index, firstNumber = searchBiggestNumber(batteryBank, 0, len(batteryBank) - 1)
    index, secondNumber = searchBiggestNumber(batteryBank, index+1, len(batteryBank))
    solution += int(firstNumber + secondNumber)
    

print(solution)