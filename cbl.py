def display(textToBeDisplayed):
	print(textToBeDisplayed)

def ask(textToBeAsked):
	input(textToBeAsked)

def countWord(sentence, wordToLookFor):
	print(sentence.count(wordToLookFor))

def reverse(string):
	print(string[::-1])


def repeatText(wordToBeRepeated, numOfTimes):
    resultOfWordToBeRepeated = wordToBeRepeated * numOfTimes
    print(resultOfWordToBeRepeated)




def askWithAnswer(question, questionAnswer):
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
        print ("Made by Jeff Lim in 2019 as a Github project.")


def documentation():
	print("Download the free documentation at jefflim076@wixsite.com/rewind ")
