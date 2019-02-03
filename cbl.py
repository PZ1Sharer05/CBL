def randomTakeNumbers(n1, lastn):
	from random import randint
	randomNum = randint(n1, lastn)



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
		print("Yes " + wordToSee + " is in " + text + ".")
	else:
		print ("Not in text.")


def reverse(string):
	print(string[::-1])


def repeatText(wordToBeRepeated, numOfTimes):
    resultOfWordToBeRepeated = wordToBeRepeated * numOfTimes
    print(resultOfWordToBeRepeated)




def askWithAnswer(question, questionAnswer):
	if questionAnswer == "":
		print("Absence of Value is not Allowed.")
	else:
        	questionToBeAsked = input(question)
        	if questionToBeAsked == questionAnswer:
                	print ("Thats the correct answer")
        	else:
                	print ("Wrong answer")

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
