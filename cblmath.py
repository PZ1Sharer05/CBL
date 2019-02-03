pi = 3.14
full_pi = 3.14285714286



def centimeterToMeter(valueOfCmToBeChangedToM):
    print (valueOfCmToBeChangedToM / 100)


def meterToCentimeter(valueOfMeterToBeChangedToCm):
    print (valueOfMeterToBeChangedToCm * 100)


def centimeterToKilometer(valueOfCentimeterToBeChangedToKm):
    print (valueOfCentimeterToBeChangedToKm / 100000)


def kilometerToCentimeter(valueOfKilometerToBeChangedToCm):
    print (valueOfKilometerToBeChangedToCm * 100000)


def meterToKilometer(valueOfMeterToBeChangedToKm):
    print (valueOfMeterToBeChangedTokilometer / 1000)


def kilometerToMeter(valueOfKilometerToBeChangedToM):
    print (valueOfKilometerToBeChangedToMeter * 1000)


def millimeterToKilometer(valueOfMillimeterToBeChangedToKm):
    print (valueOfMillimeterToBeChangedToKm / 1000000)


def kilometerToMillimeter(valueOfKilometerToBeChangedToMm):
    print (valueOfMillimeterToBeChangedToKm * 1000000)

#Circle
def circle(radius, operationToDoInCircle, typeOfCircle):
    if operationToDoInCircle == "area":
        #area
        #Type of Circle
        if typeOfCircle == "Full":
            return pi * radius * radius
        elif typeOfCircle == "Semicircle":
            return pi * 0.5 * radius * radius
        elif typeOfCircle == "Quarter circle":
            return pi * 0.25 * radius * radius
        else:
            print ("Not a supported circle type.")
    elif operationToDoInCircle == "perimeter":
        #perimeter
        if typeOfCircle == "Full":
            return pi * radius * 2
        elif typeOfCircle == "Semicircle":
            return (0.5 * pi * radius * 2) + radius * 2
        elif typeOfCircle == "Quarter circle":
            return (pi * 0.25 * radius * 2) + radius * 2
        else:
            print ("Not a supported circle type")


    else:
        print ("Not an operation")
#Square
def square(side, operationToDoInSquare):
    if operationToDoInSquare == "area":
        return side ** 2
    elif operationToDoInSquare == "perimeter":
        return side * 4
#Rectangle
def rectangle(length, breadth, operationToDo):
    if operationToDo == "area":
        return length * breadth
    elif operationToDo == "perimeter":
        return  (length + breadth) * 2
    else:
        print ("Not an operation. Only operations are: area \n perimeter")


#Triangle
def areaOfTriangle(base, height):
    return base * height * 0.5
def perimeterOfTriangle(side,nextSide,lastSide,type):
    if type == "Equilateral":
        return side * 3
    elif type == "Isosceles":
        return side + nextSide * 2
    elif type == "Scalene":
        return side + nextSide + lastSide
    else:
        print ("Error, not a triangle type, the only types are: \n Equilateral \n Isosceles \n and Scalene")

#Volumes
def volumeOfCube(side):
    return side ** 3

def volumeOfCuboid(lengthOfCuboid, heightOfCuboid, breadthOfCuboid):
    return lengthOfCuboid * heightOfCuboid * breadthOfCuboid

def findVolumeOfCylinder(base, height):
     print (int(3.14 * base * base * height))


def findVolumeOfPyramid(baseLengthOfPyramid, baseWidthOfPyramid, heightOfPyramid):
    print (int((baseLengthOfPyramid * baseWidthOfPyramid * heightOfPyramid) / 3))
