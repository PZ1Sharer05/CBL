#All made variables are stored here
full_pi = 3.142857142857143
pi = 3.14







#All functions are in here

def display(textToBeDisplayed):
	print(textToBeDisplayed)


def ask(textToBeAsked):
	a = input(textToBeAsked)



def reverse(string):
	print(string[::-1])


def repeatText(wordToBeRepeated, numOfTimes):
    resultOfWordToBeRepeated = wordToBeRepeated * numOfTimes
    print(resultOfWordToBeRepeated)

def findSum(numone, numtwo):
        print(numone + numtwo)



def findDifference(numdone, numdtwo):
        print(numdone - numdtwo)




def findProduct(nummone, nummtwo):
        print(nummone * nummtwo)



def findQuotient(numqone, numqtwo):
        print(numqone / numqtwo)




def findRemainder(numrone, numrtwo):
        return numrone % numrtwo



def askWithAnswer(question, answer):
        babfdas = input(question)
        if babfdas == answer:
                print ("Thats the correct answer")
        else:
                print ("Wrong answer")



def showNumber(numberToBeShown):
        return numberToBeShown

def areaOfCircle(radius):
        return 3.14 * radius * radius


def perimeterOfCircle(diameter):
        return 3.14 * diameter


def calculateLengthOfWord(word):
        return len(word)

def upperCase(wordToBeUpper):
        return wordToBeUpper.upper()


def lowerCase(wordToBeLower):
        return wordToBeLower.lower()

def credits():
        print ("Made by Jeff Lim in 2019 as a Github project.")




def meterToCentimeter(valueOFMeter):
        print(valueOFMeter * 100)


def centimeterToMeter(valueOFCm):
        print(valueOFCm / 100)

def kilometerToMeter(valueOfKm):
	print(valueOfKm * 1000)
def meterToKilometer(valueOfMeterToBeChangedToKilometers):
	print(valueOfMeterToBeChangedToKilometers / 1000)
