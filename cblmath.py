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
