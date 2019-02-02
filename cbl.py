def randomTakeNumbers(n1, lastn):
	from random import randint
	randomNum = randint(n1, lastn)



def display(textToBeDisplayed):
	print(textToBeDisplayed)


def split(sentenceToBeSplit):
	sentenceToBeSplit = sentenceToBeSplit.split()
	for words in sentenceToBeSplit:
		print (words)
def ask(textToBeAsked):
	input(textToBeAsked)

def countWord(sentence, wordToLookFor):
	print(sentence.count(wordToLookFor))


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

def length(word):
        print (len(word))

def changeSizeOfWord(wordToBeChangedInSize, upperOrLower):
	if upperOrLower == "upper":
		print (wordToBeChangedInSize.upper())
	elif upperOrLower == "lower":
		print(wordToBeChangedInSize.lower())




def returnValue(valueToBeReturned):
	return  valueToBeReturned


def credits():
        print ("Made by Jeff Lim in 2019 as a Github project. \n Change of CBL Programming Language Library is allowed. ")


def documentation():
	print("Download the free documentation at jefflim076@wixsite.com/rewind ")
