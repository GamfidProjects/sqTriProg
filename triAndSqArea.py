import math

#methods
def getSquareArea(a):
    return a ** 2;
def getTriangleArea(a, b, c):
    hp = (a + b + c) / 2
    TriArea = math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))
    return TriArea

#programs

#tri area program
def triAreaProgram():
    sidesStr = input("Enter triangle sides: ")
    sidesStr = sidesStr.replace(" ", "")
    sidesStrList = sidesStr.split(",")

    #checking whether the string is correct and writing the value
    try:
        sidesList = [];
        for i in range(0, len(sidesStrList)):
            sidesList.append(float(sidesStrList[i]))
    except:
        print("Error: The sides were entered in an incorrect format!")
        return 0

    #if the sides count doesnt happen to be 3, display error and exit
    if len(sidesStrList) != 3:
        print(f"Error: There are {len(sidesStrList)} sides. A triangle has to have 3.")
        return 0;

    try:
        sideA = sidesList[0]
        sideB = sidesList[1]
        sideC = sidesList[2]

        if not (sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA):
            print("Invalid sides!")
            return 0


        triArea = getTriangleArea(sideA, sideB, sideC)
    except:
        print("Error!")
        return 0

    triAreaToOutput = str(triArea)

    if (triArea % 1) == 0:
        triAreaToOutput = int(triArea)

    print("Triangle area: ", triAreaToOutput)
    #end of the line!
    return 0
#square area program
def SqAreaProgram():
    sideStr = input("Enter square side: ")
    sideStr = sideStr.replace(" ", "")

    try:
        side = float(sideStr)
        if side % 1 == 0:
            side = int(side)
    except:
        print("Error: Incorrect format!")
        return 0

    if side <= 0:
        print("Error: Side needs to be >0!")
        return 0
    
    sqAreaToOutput = getSquareArea(side)

    print("Square area: ", sqAreaToOutput)
    #end of the line!
    return 0

#actual MAIN program
isRunning = True
while isRunning:
    while True:
        modeInput = input("Choose which shape to get the area from(1 - square, 2 - circle): ")
        if modeInput == "1":
            SqAreaProgram()
            break
        elif modeInput == "2":
            triAreaProgram()
            break
        else:
            print("Invalid input!")
        continue
    notContinued = True
    while notContinued:
        continueQ = input("Continue? Enter y/n: ")
        if continueQ == "y":
            notContinued = False
            continue
        elif continueQ == "n":
            notContinued = False
            isRunning = False
        else:
            print("Not an option!")
        
    




print("Exiting program")
#read a line so the program DOESNT CLOSE right away
input("Press enter to close...")
#fuck this shit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!