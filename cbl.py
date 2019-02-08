def randomTakeNumbers(n1, lastn):
	from random import randint
	randomNum = randint(n1, lastn)
	return randomNum


def randomTakeFromArray(arrayToBeRandommized):
	import random
	randomGeneratedChoice = random.choice(arrayToBeRandommized)
	return randomGeneratedChoice
def interger(intergerValue):
	return int(intergerValue)

def string(stringValue):
	return str(stringValue)

def floatingPoint(floatNum):
	return float(floatNum)

def showShortText(shortText):
	idkfdgbssddddddddd = len(shortText)
	if idkfdgbssddddddddd > 500:
		print ("Not short text, short text must have maximum of 500 characters. \nConsider using showTextFunction.")
	else:
		print(shortText)


def showText(textToBeShown):
	print(textToBeShown)


def split(sentenceToBeSplit):
	sentenceToBeSplit = sentenceToBeSplit.split()
	return sentenceToBeSplit


def ask(textToBeAsked):
	input(textToBeAsked)

def countWord(sentence, wordToLookFor):
	return sentence.count(wordToLookFor)


def checkIfWordInText(text, wordToSee):
	if wordToSee in text:
		return True
	else:
		return False

def reverse(string):
	return string[::-1]


def repeatText(wordToBeRepeated, numOfTimes):
    resultOfWordToBeRepeated = wordToBeRepeated * numOfTimes
    return resultOfWordToBeRepeated





def lengthOfWord(word):
	return len(word)


def changeSizeOfWord(wordToBeChangedInSize, upperOrLower):
	if upperOrLower == "upper":
		return wordToBeChangedInSize.upper()
	elif upperOrLower == "lower":
		return wordToBeChangedInSize.lower()
	else:
		print ("Not a supported case type.")





def credits():
        print ("Made by Jeff Lim in 2019 as a Github project. Licensed under the MIT License, copyright permissions are required.")
