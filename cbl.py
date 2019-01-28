#All made variables are stored here
full_pi = 3.142857142857143
pi = 3.14








#All functions are in here

def display(textToBeDisplayed):
	print(textToBeDisplayed)

	
def ask(textToBeAsked):
	a = input(textToBeAsked)
	
	
	
def reverse(string):
	return string[::-1]


def repeatText(wordToBeRepeated, numOfTimes):
    resultOfWordToBeRepeated = wordToBeRepeated * numOfTimes
    print(resultOfWordToBeRepeated)

def findSum(numone, numtwo):
        return numone + numtwo



def findDifference(numdone, numdtwo):
        return numdone - numdtwo




def findProduct(nummone, nummtwo):
        return nummone * nummtwo



def findQuotient(numqone, numqtwo):
        return numqone / numqtwo




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


def origins():
        print ("Originally a dream, Jeff Lim invented the CBL as a language kids should use for programming \n I made the language fully kid friendly and I wish the kids would understand how to use CBL as well as the father of CBL, Python. \n Since Python is the father of CBL, understanding CBL means understanding Python. To read the full documentation, visit our website.")
