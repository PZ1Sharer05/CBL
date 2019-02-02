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
    print (valurOfMillimeterToBeChangedToKm / 1000000)


def kilometerToMillimeter(valueOfKilometerToBeChangedToMm):
    print (valurOfMillimeterToBeChangedToKm * 1000000)


def areaOfCircle(radius, piType):
    if piType == "full_pi":
        print (int(full_pi * radius * radius))
    elif piType == "pi":
        print (int(pi * radius * radius))


def findAreaOfSquare(side):
    print (side ** 2)


def findAreaOfRectangle(length, breadth):
    print (length * breadth)


def findAreaOfTriangle(base, height):
    print (base * height * 0.5)

def findVolumeOfCube(sideOfCube):
    print (sideOfCube ** 3)

def findVolumeOfCuboid(length, heightOfCuboid, breadthOfCuboid):
    print (length * heightOfCuboid * breadthOfCuboid)

def findVolumeOfCylinder(base, height):
     print (int(3.14 * base * base * height))


def findVolumeOfPyramid(baseLengthOfPyramid, baseWidthOfPyramid, heightOfPyramid):
    print (int((baseLengthOfPyramid * baseWidthOfPyramid * heightOfPyramid) / 3))
