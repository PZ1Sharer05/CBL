def randomTakeNumbers(n1, lastn):
	from random import randint
	randomNum = randint(n1, lastn)
	return randomNum


def display(textToBeDisplayed):
	print(textToBeDisplayed)


def split(sentenceToBeSplit):
	sentenceToBeSplit = sentenceToBeSplit.split()
	return sentenceToBeSplit


def ask(textToBeAsked):
	input(textToBeAsked)

def countWord(sentence, wordToLookFor):
	return sentence.count(wordToLookFor)


def seeIfWordInText(text, wordToSee):
	if wordToSee in text:
		return True
	else:
		return False

def reverse(string):
	return string[::-1]


def repeatText(wordToBeRepeated, numOfTimes):
    resultOfWordToBeRepeated = wordToBeRepeated * numOfTimes
    return resultOfWordToBeRepeated




def askWithAnswer(question, questionAnswer, messageToShowWhenValueIsEqual, messageToShowWhenValueIsNotEqual):
	if questionAnswer == "":
		print("Absence of Value is not Allowed.")
	else:
        	questionToBeAsked = input(question)
        	if questionToBeAsked == questionAnswer:
                	return messageToShowWhenValueIsEqual
        	else:
                	return messageToShowWhenValueIsNotEqual

def lengthOfWord(word):
	return len(word)


def changeSizeOfWord(wordToBeChangedInSize, upperOrLower):
	if upperOrLower == "upper":
		return wordToBeChangedInSize.upper()
	elif upperOrLower == "lower":
		return wordToBeChangedInSize.lower()






def credits():
        print ("Made by Jeff Lim in 2019 as a Github project. Licensed under the MIT License, copyright permissions are required.")


def documentation():
	print("The documentation is in the github file: CBL Documentation.docx")
