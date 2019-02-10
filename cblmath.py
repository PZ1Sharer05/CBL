pi = 3.14
full_pi = 3.14285714286


def addNumbers(n1, n2):
    return n1 + n2
def subtract(ns1, ns2):
    return ns1 - ns2
def multiply(nm1, nm2):
    return nm1 * nm2
def divide(nd1, nd2, showRemainder):
    if showRemainder == True:
        return nd1 / nd2
        return nd1 % nd2
    elif showRemainder == False:
        return nd1 / nd2
        



def evenOrOdd(number, typeToCheck):
    if typeToCheck == "even":
        if number % 2 == 0:
            return True
        else:
            return False
    elif typeToCheck == "odd":
        if number % 2 == 1:
            return True
        else:
            return False
    else:
        print ("Error, not part of function.")

def centimeterToMeter(valueOfCmToBeChangedToM):
    return valueOfCmToBeChangedToM / 100


def meterToCentimeter(valueOfMeterToBeChangedToCm):
    return valueOfMeterToBeChangedToCm * 100


def centimeterToKilometer(valueOfCentimeterToBeChangedToKm):
    return valueOfCentimeterToBeChangedToKm / 100000


def kilometerToCentimeter(valueOfKilometerToBeChangedToCm):
    return valueOfKilometerToBeChangedToCm * 100000


def meterToKilometer(valueOfMeterToBeChangedToKm):
    return valueOfMeterToBeChangedTokilometer / 1000


def kilometerToMeter(valueOfKilometerToBeChangedToM):
    return valueOfKilometerToBeChangedToMeter * 1000


def millimeterToKilometer(valueOfMillimeterToBeChangedToKm):
    return valueOfMillimeterToBeChangedToKm / 1000000


def kilometerToMillimeter(valueOfKilometerToBeChangedToMm):
    return valueOfMillimeterToBeChangedToKm * 1000000

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


def squareOrRectangle(shape, operationToDo, lengthOfShape, breadthOfShape):
    if shape == "square":
        #square
        if lengthOfShape == breadthOfShape:

            if operationToDo == "area":
                #areaOfSquare
                return lengthOfShape ** 2
            elif operationToDo == "perimeter":
                #perimeterOfSquare
                return  lengthOfShape * 4
            else:
                print ("Not an operation")
        else:
            print ("Not a square")
    elif shape == "rectangle":
        #rectangle
        if operationToDo == "area":
            #areaOfRectangle
            return lengthOfShape * breadthOfShape
        elif operationToDo == "perimeter":
            #perimeterOfRectangle
            return  (lengthOfShape + breadthOfShape) * 2
        else:
            print ("Not an operation")
    else:
        print ("Not a valid shape for function")

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
def volumeOfCubeOrCuboid(lengthOfCuboid, breadthOfCuboid, heightOfCuboid, shape):
    if shape == "Cube":
        if lengthOfCuboid == breadthOfCuboid and lengthOfCuboid == heightOfCuboid and breadthOfCuboid == heightOfCuboid:
            return lengthOfCuboid ** 3
        else:
            print ("Not a cube")
    elif shape == "Cuboid":
        return lengthOfCuboid * heightOfCuboid * breadthOfCuboid
    else:
        print ("Not a cube or cuboid")

def findVolumeOfCylinder(base, height):
     return 3.14 * base * base * height


def findVolumeOfPyramid(baseLengthOfPyramid, baseWidthOfPyramid, heightOfPyramid):
    return (baseLengthOfPyramid * baseWidthOfPyramid * heightOfPyramid) / 3
