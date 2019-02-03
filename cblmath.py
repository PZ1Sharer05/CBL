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
def areaOfCircle(radius, circleType):
    if circleType == "Full":
        return 3.14 * radius * radius
    elif circleType == "Semicircle":
        return 0.5 * 3.14 * radius * radius
    elif circleType == "Quarter circle":
        return  0.25 * 3.14 * radius * radius
    else:
        print ("Error, not a circle type value, please choose between \n Full \n Semicircle \n and Quarter circle")

def findCircumference(diameter):
    print (3.14 * diameter)

#Square
def findAreaOfSquare(side):
    print (side ** 2)
def findPerimeterOfSquare(side):
    print (side * 4)

#Rectangle
def findAreaOfRectangle(length, breadth):
    return length * breadth

def findPerimeterOfRectangle(length, breadth):
    return (length + breadth) * 2




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
